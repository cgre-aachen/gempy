﻿from dataclasses import dataclass

import gempy_engine.core.data.grid
from gempy_engine.core.data import InterpolationOptions
from gempy_engine.core.data.input_data_descriptor import InputDataDescriptor
from gempy_engine.core.data.interpolation_input import InterpolationInput
from .structural_frame import StructuralFrame
from .transforms import Transform
from ..grid import Grid

"""
TODO:
    - [ ] StructuralFrame will all input points chunked on Elements. Here I will need a property to put all
    together to feed to InterpolationInput

"""


@dataclass
class GeoModelMeta:
    name: str
    creation_date: str
    last_modification_date: str
    owner: str


@dataclass(init=False)
class GeoModel:
    meta: GeoModelMeta
    structural_frame: StructuralFrame
    grid: Grid  # * This is the general gempy grid
    transform: Transform
    
    # region GemPy engine data types
    _interpolationInput: InterpolationInput  # * This has to be fed by structural_frame
    interpolation_options: InterpolationOptions  # * This has to be fed by USER
    _input_data_descriptor: InputDataDescriptor  # * This has to be fed by structural_frame
    interpolation_grid: gempy_engine.core.data.grid.Grid
    
    # endregion

    def __init__(self, name: str, structural_frame: StructuralFrame, grid: Grid,
                 interpolation_options: InterpolationOptions):
        # TODO: Fill the arguments properly
        self.meta = GeoModelMeta(
            name=name,
            creation_date=None,
            last_modification_date=None,
            owner=None
        )
        
        self.structural_frame = structural_frame  # ? This could be Optional

        self.grid = grid
        self.interpolation_options = interpolation_options
        self.transform = Transform()
