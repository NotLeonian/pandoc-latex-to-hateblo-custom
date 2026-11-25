"""Local type declarations for panflute 3.0.0's io module."""

from collections.abc import Callable, Iterable
from typing import Concatenate

from _typeshed import SupportsRead, SupportsWrite
from panflute.base import Element
from panflute.elements import Doc

# list is invariant. A callback may return a list of an Element subclass.
type _Action[T: Element] = Callable[
    Concatenate[Element, Doc, ...], Element | list[T] | None
]

def load(input_stream: SupportsRead[str] | None = None) -> Doc: ...
def dump(doc: Doc, output_stream: SupportsWrite[str] | None = None) -> None: ...
def run_filters[T: Element](
    actions: Iterable[_Action[T]],
    prepare: Callable[[Doc], object] | None = None,
    finalize: Callable[[Doc], object] | None = None,
    input_stream: SupportsRead[str] | None = None,
    output_stream: SupportsWrite[str] | None = None,
    doc: Doc | None = None,
    stop_if: Callable[[Element], bool] | None = None,
    **kwargs: object,
) -> Doc | None: ...
def run_filter[T: Element](
    action: _Action[T],
    prepare: Callable[[Doc], object] | None = None,
    finalize: Callable[[Doc], object] | None = None,
    input_stream: SupportsRead[str] | None = None,
    output_stream: SupportsWrite[str] | None = None,
    doc: Doc | None = None,
    stop_if: Callable[[Element], bool] | None = None,
    **kwargs: object,
) -> Doc | None: ...

toJSONFilters = run_filters
toJSONFilter = run_filter
