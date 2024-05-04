import types
import zipimport
from _typeshed import Incomplete, StrPath, Unused
from collections.abc import Callable, Generator, Iterable, Iterator, Sequence
from io import BytesIO
from itertools import chain
from pkgutil import get_importer as get_importer
from re import Pattern
from typing import IO, Any, ClassVar, Final, Literal, NoReturn, Protocol, TypeVar, overload, type_check_only
from typing_extensions import Self, TypeAlias
from zipfile import ZipInfo

from ._vendored_packaging import requirements as packaging_requirements, version as packaging_version

_T = TypeVar("_T")
_D = TypeVar("_D", bound=Distribution)
_NestedStr: TypeAlias = str | Iterable[_NestedStr]
_StrictInstallerType: TypeAlias = Callable[[Requirement], _D]
_InstallerType: TypeAlias = Callable[[Requirement], Distribution | None] | None
_PkgReqType: TypeAlias = str | Requirement
_EPDistType: TypeAlias = Distribution | _PkgReqType
_MetadataType: TypeAlias = IResourceProvider | None
_ResolvedEntryPoint: TypeAlias = Any  # Can be any attribute in the module
_ModuleLike: TypeAlias = object | types.ModuleType  # Any object that optionally has __loader__ or __file__, usually a module
_ProviderFactoryType: TypeAlias = Callable[[_ModuleLike], IResourceProvider]
_DistFinderType: TypeAlias = Callable[[_T, str, bool], Iterable[Distribution]]
_NSHandlerType: TypeAlias = Callable[[_T, str, str, types.ModuleType], str | None]
_ResourceStream: TypeAlias = Incomplete  # A readable file-like object

__all__ = [
    "require",
    "run_script",
    "get_provider",
    "get_distribution",
    "load_entry_point",
    "get_entry_map",
    "get_entry_info",
    "iter_entry_points",
    "resource_string",
    "resource_stream",
    "resource_filename",
    "resource_listdir",
    "resource_exists",
    "resource_isdir",
    "declare_namespace",
    "working_set",
    "add_activation_listener",
    "find_distributions",
    "set_extraction_path",
    "cleanup_resources",
    "get_default_cache",
    "Environment",
    "WorkingSet",
    "ResourceManager",
    "Distribution",
    "Requirement",
    "EntryPoint",
    "ResolutionError",
    "VersionConflict",
    "DistributionNotFound",
    "UnknownExtra",
    "ExtractionError",
    "PEP440Warning",
    "parse_requirements",
    "parse_version",
    "safe_name",
    "safe_version",
    "get_platform",
    "compatible_platforms",
    "yield_lines",
    "split_sections",
    "safe_extra",
    "to_filename",
    "invalid_marker",
    "evaluate_marker",
    "ensure_directory",
    "normalize_path",
    "EGG_DIST",
    "BINARY_DIST",
    "SOURCE_DIST",
    "CHECKOUT_DIST",
    "DEVELOP_DIST",
    "IMetadataProvider",
    "IResourceProvider",
    "FileMetadata",
    "PathMetadata",
    "EggMetadata",
    "EmptyProvider",
    "empty_provider",
    "NullProvider",
    "EggProvider",
    "DefaultProvider",
    "ZipProvider",
    "register_finder",
    "register_namespace_handler",
    "register_loader_type",
    "fixup_namespace_packages",
    "get_importer",
    "PkgResourcesDeprecationWarning",
    "run_main",
    "AvailableDistributions",
]

@type_check_only
class _ZipLoaderModule(Protocol):
    __loader__: zipimport.zipimporter

def declare_namespace(packageName: str) -> None: ...
def fixup_namespace_packages(path_item: str, parent: str | None = None) -> None: ...

class WorkingSet:
    entries: list[str]
    def __init__(self, entries: Iterable[str] | None = None) -> None: ...
    def add_entry(self, entry: str) -> None: ...
    def __contains__(self, dist: Distribution) -> bool: ...
    def find(self, req: Requirement) -> Distribution | None: ...
    def iter_entry_points(self, group: str, name: str | None = None) -> Generator[EntryPoint, None, None]: ...
    def run_script(self, requires: str, script_name: str) -> None: ...
    def __iter__(self) -> Iterator[Distribution]: ...
    def add(self, dist: Distribution, entry: str | None = None, insert: bool = True, replace: bool = False) -> None: ...
    @overload
    def resolve(  # type: ignore[overload-overlap]
        self,
        requirements: Iterable[Requirement],
        env: Environment | None,
        installer: _StrictInstallerType[_D],
        replace_conflicting: bool = False,
        extras: tuple[str, ...] | None = None,
    ) -> list[_D]: ...
    @overload
    def resolve(  # type: ignore[overload-overlap]
        self,
        requirements: Iterable[Requirement],
        env: Environment | None = None,
        *,
        installer: _StrictInstallerType[_D],
        replace_conflicting: bool = False,
        extras: tuple[str, ...] | None = None,
    ) -> list[_D]: ...
    @overload
    def resolve(
        self,
        requirements: Iterable[Requirement],
        env: Environment | None = None,
        installer: _InstallerType = None,
        replace_conflicting: bool = False,
        extras: tuple[str, ...] | None = None,
    ) -> list[Distribution]: ...
    @overload
    def find_plugins(  # type: ignore[overload-overlap]
        self, plugin_env: Environment, full_env: Environment | None, installer: _StrictInstallerType[_D], fallback: bool = True
    ) -> tuple[list[_D], dict[Distribution, Exception]]: ...
    @overload
    def find_plugins(  # type: ignore[overload-overlap]
        self,
        plugin_env: Environment,
        full_env: Environment | None = None,
        *,
        installer: _StrictInstallerType[_D],
        fallback: bool = True,
    ) -> tuple[list[_D], dict[Distribution, Exception]]: ...
    @overload
    def find_plugins(
        self,
        plugin_env: Environment,
        full_env: Environment | None = None,
        installer: _InstallerType = None,
        fallback: bool = True,
    ) -> tuple[list[Distribution], dict[Distribution, Exception]]: ...
    def require(self, *requirements: _NestedStr) -> Sequence[Distribution]: ...
    def subscribe(self, callback: Callable[[Distribution], object], existing: bool = True) -> None: ...

working_set: WorkingSet
require = working_set.require
iter_entry_points = working_set.iter_entry_points
add_activation_listener = working_set.subscribe
run_script = working_set.run_script
run_main = run_script

class Environment:
    def __init__(
        self, search_path: Sequence[str] | None = None, platform: str | None = ..., python: str | None = ...
    ) -> None: ...
    def can_add(self, dist: Distribution) -> bool: ...
    def remove(self, dist: Distribution) -> None: ...
    def scan(self, search_path: Sequence[str] | None = None) -> None: ...
    def __getitem__(self, project_name: str) -> list[Distribution]: ...
    def add(self, dist: Distribution) -> None: ...
    @overload
    def best_match(
        self, req: Requirement, working_set: WorkingSet, installer: _StrictInstallerType[_D], replace_conflicting: bool = False
    ) -> _D: ...
    @overload
    def best_match(
        self, req: Requirement, working_set: WorkingSet, installer: _InstallerType = None, replace_conflicting: bool = False
    ) -> Distribution | None: ...
    @overload
    def obtain(self, requirement: Requirement, installer: _StrictInstallerType[_D]) -> _D: ...  # type: ignore[overload-overlap]
    @overload
    def obtain(self, requirement: Requirement, installer: Callable[[Requirement], None] | None = None) -> None: ...
    @overload
    def obtain(self, requirement: Requirement, installer: _InstallerType = None) -> Distribution | None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __iadd__(self, other: Distribution | Environment) -> Self: ...
    def __add__(self, other: Distribution | Environment) -> Self: ...

AvailableDistributions = Environment

def parse_requirements(strs: _NestedStr) -> Iterator[Requirement]: ...

class RequirementParseError(packaging_requirements.InvalidRequirement): ...

class Requirement(packaging_requirements.Requirement):
    unsafe_name: str
    project_name: str
    key: str
    # packaging.requirements.Requirement uses a set for its extras. setuptools/pkg_resources uses a variable-length tuple
    extras: tuple[str, ...]  # type: ignore[assignment]
    specs: list[tuple[str, str]]
    def __init__(self, requirement_string: str) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __contains__(self, item: Distribution | str | tuple[str, ...]) -> bool: ...
    @staticmethod
    def parse(s: str | Iterable[str]) -> Requirement: ...

def load_entry_point(dist: _EPDistType, group: str, name: str) -> _ResolvedEntryPoint: ...
@overload
def get_entry_map(dist: _EPDistType, group: None = None) -> dict[str, dict[str, EntryPoint]]: ...
@overload
def get_entry_map(dist: _EPDistType, group: str) -> dict[str, EntryPoint]: ...
def get_entry_info(dist: _EPDistType, group: str, name: str) -> EntryPoint | None: ...

class EntryPoint:
    name: str
    module_name: str
    attrs: tuple[str, ...]
    extras: tuple[str, ...]
    dist: Distribution | None
    def __init__(
        self, name: str, module_name: str, attrs: Iterable[str] = (), extras: Iterable[str] = (), dist: Distribution | None = None
    ) -> None: ...
    @overload
    def load(
        self, require: Literal[True] = True, env: Environment | None = None, installer: _InstallerType = None
    ) -> _ResolvedEntryPoint: ...
    @overload
    def load(self, require: Literal[False], *args: Unused, **kwargs: Unused) -> _ResolvedEntryPoint: ...
    def resolve(self) -> _ResolvedEntryPoint: ...
    def require(self, env: Environment | None = None, installer: _InstallerType = None) -> None: ...
    pattern: ClassVar[Pattern[str]]
    @classmethod
    def parse(cls, src: str, dist: Distribution | None = None) -> Self: ...
    @classmethod
    def parse_group(cls, group: str, lines: _NestedStr, dist: Distribution | None = None) -> dict[str, Self]: ...
    @classmethod
    def parse_map(
        cls, data: str | Iterable[str] | dict[str, str | Iterable[str]], dist: Distribution | None = None
    ) -> dict[str, dict[str, Self]]: ...

def find_distributions(path_item: str, only: bool = False) -> Generator[Distribution, None, None]: ...
@overload
def get_distribution(dist: _D) -> _D: ...
@overload
def get_distribution(dist: _PkgReqType) -> Distribution: ...

PY_MAJOR: Final[str]
EGG_DIST: Final = 3
BINARY_DIST: Final = 2
SOURCE_DIST: Final = 1
CHECKOUT_DIST: Final = 0
DEVELOP_DIST: Final = -1

class ResourceManager:
    extraction_path: str | None
    cached_files: Incomplete
    def resource_exists(self, package_or_requirement: _PkgReqType, resource_name: str) -> bool: ...
    def resource_isdir(self, package_or_requirement: _PkgReqType, resource_name: str) -> bool: ...
    def resource_filename(self, package_or_requirement: _PkgReqType, resource_name: str) -> str: ...
    def resource_stream(self, package_or_requirement: _PkgReqType, resource_name: str) -> IO[bytes]: ...
    def resource_string(self, package_or_requirement: _PkgReqType, resource_name: str) -> bytes: ...
    def resource_listdir(self, package_or_requirement: _PkgReqType, resource_name: str) -> list[str]: ...
    def extraction_error(self) -> NoReturn: ...
    def get_cache_path(self, archive_name: str, names: Iterable[str] = ()) -> str: ...
    def postprocess(self, tempname: str, filename: str) -> None: ...
    def set_extraction_path(self, path: str) -> None: ...
    def cleanup_resources(self, force: bool = False) -> list[str]: ...

__resource_manager: ResourceManager  # Doesn't exist at runtime
resource_exists = __resource_manager.resource_exists
resource_isdir = __resource_manager.resource_isdir
resource_filename = __resource_manager.resource_filename
resource_stream = __resource_manager.resource_stream
resource_string = __resource_manager.resource_string
resource_listdir = __resource_manager.resource_listdir
set_extraction_path = __resource_manager.set_extraction_path
cleanup_resources = __resource_manager.cleanup_resources

@overload
def get_provider(moduleOrReq: str) -> IResourceProvider: ...
@overload
def get_provider(moduleOrReq: Requirement) -> Distribution: ...

class IMetadataProvider(Protocol):
    def has_metadata(self, name: str) -> bool: ...
    def get_metadata(self, name: str) -> str: ...
    def get_metadata_lines(self, name: str) -> Iterator[str]: ...
    def metadata_isdir(self, name: str) -> bool: ...
    def metadata_listdir(self, name: str) -> list[str]: ...
    def run_script(self, script_name: str, namespace: dict[str, Any]) -> None: ...

class ResolutionError(Exception): ...

class DistributionNotFound(ResolutionError):
    def __init__(self, req: Requirement, requirers: set[str] | None, /, *args: object) -> None: ...
    @property
    def req(self) -> Requirement: ...
    @property
    def requirers(self) -> set[str] | None: ...
    @property
    def requirers_str(self) -> str: ...
    def report(self) -> str: ...

class VersionConflict(ResolutionError):
    def __init__(self, dist: Distribution, req: Requirement, /, *args: object) -> None: ...
    @property
    def dist(self) -> Distribution: ...
    @property
    def req(self) -> Requirement: ...
    def report(self) -> str: ...
    def with_context(self, required_by: set[str]) -> Self | ContextualVersionConflict: ...

class ContextualVersionConflict(VersionConflict):
    def __init__(self, dist: Distribution, req: Requirement, required_by: set[str], /, *args: object) -> None: ...
    @property
    def required_by(self) -> set[str]: ...

class UnknownExtra(ResolutionError): ...

class ExtractionError(Exception):
    manager: ResourceManager
    cache_path: str
    original_error: BaseException | None

def register_finder(importer_type: type[_T], distribution_finder: _DistFinderType[_T]) -> None: ...
def register_loader_type(loader_type: type[_ModuleLike], provider_factory: _ProviderFactoryType) -> None: ...
def register_namespace_handler(importer_type: type[_T], namespace_handler: _NSHandlerType[_T]) -> None: ...

class IResourceProvider(IMetadataProvider, Protocol):
    def get_resource_filename(self, manager: ResourceManager, resource_name: str) -> StrPath: ...
    def get_resource_stream(self, manager: ResourceManager, resource_name: str) -> _ResourceStream: ...
    def get_resource_string(self, manager: ResourceManager, resource_name: str) -> bytes: ...
    def has_resource(self, resource_name: str) -> bool: ...
    def resource_isdir(self, resource_name: str) -> bool: ...
    def resource_listdir(self, resource_name: str) -> list[str]: ...

def invalid_marker(text: str) -> SyntaxError | Literal[False]: ...
def evaluate_marker(text: str, extra: Incomplete | None = None) -> bool: ...

class NullProvider:
    egg_name: str | None
    egg_info: str | None
    loader: types._LoaderProtocol | None
    module_path: str | None

    def __init__(self, module: _ModuleLike) -> None: ...
    def get_resource_filename(self, manager: ResourceManager, resource_name: str) -> str: ...
    def get_resource_stream(self, manager: ResourceManager, resource_name: str) -> BytesIO: ...
    def get_resource_string(self, manager: ResourceManager, resource_name: str) -> bytes: ...
    def has_resource(self, resource_name: str) -> bool: ...
    def has_metadata(self, name: str) -> bool: ...
    def get_metadata(self, name: str) -> str: ...
    def get_metadata_lines(self, name: str) -> chain[str]: ...
    def resource_isdir(self, resource_name: str) -> bool: ...
    def metadata_isdir(self, name: str) -> bool: ...
    def resource_listdir(self, resource_name: str) -> list[str]: ...
    def metadata_listdir(self, name: str) -> list[str]: ...
    def run_script(self, script_name: str, namespace: dict[str, Any]) -> None: ...

# Doesn't actually extend NullProvider, solves a typing issue in pytype_test.py
class Distribution(NullProvider):
    PKG_INFO: ClassVar[str]
    project_name: str
    py_version: str | None
    platform: str | None
    location: str | None
    precedence: int
    def __init__(
        self,
        location: str | None = None,
        metadata: _MetadataType = None,
        project_name: str | None = None,
        version: str | None = None,
        py_version: str | None = ...,
        platform: str | None = None,
        precedence: int = 3,
    ) -> None: ...
    @classmethod
    def from_location(
        cls, location: str, basename: str, metadata: _MetadataType = None, *, precedence: int = 3
    ) -> Distribution: ...
    @property
    def hashcmp(self) -> tuple[parse_version, int, str, str | None, str, str]: ...
    def __hash__(self) -> int: ...
    def __lt__(self, other: Distribution) -> bool: ...
    def __le__(self, other: Distribution) -> bool: ...
    def __gt__(self, other: Distribution) -> bool: ...
    def __ge__(self, other: Distribution) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def key(self) -> str: ...
    @property
    def parsed_version(self) -> packaging_version.Version: ...
    @property
    def version(self) -> str: ...
    def requires(self, extras: Iterable[str] = ()) -> list[Requirement]: ...
    def activate(self, path: list[str] | None = None, replace: bool = False) -> None: ...
    def egg_name(self) -> str: ...  # type: ignore[override]  # supertype's egg_name is a variable, not a method
    @classmethod
    def from_filename(cls, filename: str, metadata: _MetadataType = None, *, precedence: int = 3) -> Distribution: ...
    def as_requirement(self) -> Requirement: ...
    def load_entry_point(self, group: str, name: str) -> _ResolvedEntryPoint: ...
    @overload
    def get_entry_map(self, group: None = None) -> dict[str, dict[str, EntryPoint]]: ...
    @overload
    def get_entry_map(self, group: str) -> dict[str, EntryPoint]: ...
    def get_entry_info(self, group: str, name: str) -> EntryPoint | None: ...
    def insert_on(self, path: list[str], loc: Incomplete | None = None, replace: bool = False) -> None: ...
    def check_version_conflict(self) -> None: ...
    def has_version(self) -> bool: ...
    def clone(self, **kw: str | int | IResourceProvider | None) -> Requirement: ...
    @property
    def extras(self) -> list[str]: ...

class DistInfoDistribution(Distribution):
    PKG_INFO: ClassVar[Literal["METADATA"]]
    EQEQ: ClassVar[Pattern[str]]

class EggProvider(NullProvider):
    egg_root: str

class DefaultProvider(EggProvider): ...

class PathMetadata(DefaultProvider):
    egg_info: str
    module_path: str
    def __init__(self, path: str, egg_info: str) -> None: ...

class ZipProvider(EggProvider):
    eagers: list[str] | None
    zip_pre: str
    # ZipProvider's loader should always be a zipimporter
    loader: zipimport.zipimporter
    def __init__(self, module: _ZipLoaderModule) -> None: ...
    @property
    def zipinfo(self) -> dict[str, ZipInfo]: ...

class EggMetadata(ZipProvider):
    loader: zipimport.zipimporter
    module_path: str
    def __init__(self, importer: zipimport.zipimporter) -> None: ...

class EmptyProvider(NullProvider):
    module_path: None
    def __init__(self) -> None: ...

empty_provider: EmptyProvider

class FileMetadata(EmptyProvider):
    path: StrPath
    def __init__(self, path: StrPath) -> None: ...

class PEP440Warning(RuntimeWarning): ...

parse_version = packaging_version.Version

def yield_lines(iterable: _NestedStr) -> chain[str]: ...
def split_sections(s: _NestedStr) -> Generator[tuple[str | None, list[str]], None, None]: ...
def safe_name(name: str) -> str: ...
def safe_version(version: str) -> str: ...
def safe_extra(extra: str) -> str: ...
def to_filename(name: str) -> str: ...
def get_build_platform() -> str: ...

get_platform = get_build_platform

def get_supported_platform() -> str: ...
def compatible_platforms(provided: str | None, required: str | None) -> bool: ...
def get_default_cache() -> str: ...
def ensure_directory(path: str) -> None: ...
def normalize_path(filename: str) -> str: ...

class PkgResourcesDeprecationWarning(Warning): ...
