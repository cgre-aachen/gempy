﻿import numpy as np

import gempy as gp
import gempy_viewer as gpv
from gempy.core.data.enumerators import ExampleModel


def test_section_grids():
    geo_model: gp.data.GeoModel = gp.generate_example_model(
        example_model=ExampleModel.ANTICLINE,
        compute_model=False
    )

    geo_model.interpolation_options.number_octree_levels = 2

    gp.set_section_grid(
        grid=geo_model.grid,
        section_dict={
            'section_SW-NE': ([250, 250], [1750, 1750], [100, 100]),
            'section_NW-SE': ([250, 1750], [1750, 250], [100, 100])
        }
    )

    gp.set_topography_from_random(
        grid=geo_model.grid,
        fractal_dimension=1.2,
        d_z=np.array([200, 1000]),
        topography_resolution=np.array([60, 60])
    )

    gp.compute_model(geo_model)
    gpv.plot_2d(
        model=geo_model,
        section_names=['section_SW-NE', 'section_NW-SE', 'topography'],
        direction=['x'], cell_number=['mid'],
        show_lith=[False, True, False, True],
        show_boundaries=[False, False, False, True],
        show_topography=True,
        show_section_traces=True  # TODO: Test this one
    )

    gpv.plot_2d(geo_model, show_boundaries=False, section_names=['topography'])
    gpv.plot_3d(
        geo_model,
        show_data=True,
        show_boundaries=True,
        show_lith=False,
        image=False
    )


def test_topogrphy_II():
    geo_model: gp.data.GeoModel = gp.generate_example_model(
        example_model=ExampleModel.TWO_AND_A_HALF_D,
        compute_model=False
    )
    
    gpv.plot_3d(
        geo_model,
        show_data=True,
        show_boundaries=True,
        show_lith=False,
        image=True
    )
    
    geo_model.interpolation_options.dual_contouring = False # TODO: Figure out what is wrong here
    gp.compute_model(geo_model)

    gpv.plot_2d(geo_model, show_boundaries=False, section_names=['topography'])
    
    gpv.plot_3d(
        geo_model,
        show_data=True,
        show_boundaries=True,
        show_lith=True,
        image=False,
        kwargs_plot_structured_grid={'opacity': .1}
    )
