# Copyright 2023-2023 the openage authors. See copying.md for legal info.
#
# pylint: disable=too-few-public-methods

"""
Organize export data (nyan objects, media, scripts, etc.)
into modpacks.
"""
from __future__ import annotations
import typing

from ....entity_object.conversion.modpack import Modpack
from ..aoc.modpack_subprocessor import AoCModpackSubprocessor

if typing.TYPE_CHECKING:
    from openage.convert.entity_object.conversion.aoc.genie_object_container\
        import GenieObjectContainer


class DE1ModpackSubprocessor:
    """
    Creates the modpacks containing the nyan files and media from the DE2 conversion.
    """

    @classmethod
    def get_modpacks(cls, full_data_set: GenieObjectContainer) -> list[Modpack]:
        """
        Return all modpacks that can be created from the gamedata.
        """
        de1_base = cls._get_aoe1_base(full_data_set)

        return [de1_base]

    @classmethod
    def _get_aoe1_base(cls, full_data_set: GenieObjectContainer) -> Modpack:
        """
        Create the aoe2-base modpack.
        """
        modpack = Modpack("de1_base")

        mod_def = modpack.get_info()

        mod_def.set_info("de1_base", "0.5", versionstr="1.0a", repo="openage")

        mod_def.add_include("data/**")

        AoCModpackSubprocessor.organize_nyan_objects(modpack, full_data_set)
        AoCModpackSubprocessor.organize_media_objects(modpack, full_data_set)

        return modpack
