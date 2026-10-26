"""Stubs for the panflute 2.3.1 API used by this project."""

from collections.abc import Callable, Iterable, Mapping, MutableSequence
from typing import Any, Literal, Self, TextIO

class Element:
    def __new__(cls, *args: Any, **kwargs: Any) -> Self: ...
    @property
    def prev(self) -> Element | None: ...
    @property
    def next(self) -> Element | None: ...

class Inline(Element): ...
class Block(Element): ...

class Doc(Element):
    content: MutableSequence[Block]
    format: str
    def __init__(
        self,
        *args: Block,
        metadata: Mapping[str, Any] = ...,
        format: str = ...,
        api_version: tuple[int, ...] = ...,
    ) -> None: ...
    def get_metadata(
        self, key: str = ..., default: Any = ..., builtin: bool = ...
    ) -> Any: ...

class Plain(Block):
    content: MutableSequence[Inline]
    def __init__(self, *args: Inline) -> None: ...

class Para(Block):
    content: MutableSequence[Inline]
    def __init__(self, *args: Inline) -> None: ...

class SoftBreak(Inline): ...

class Str(Inline):
    text: str
    def __init__(self, text: str) -> None: ...

class RawBlock(Block):
    text: str
    format: str
    def __init__(self, text: str, format: str = ...) -> None: ...

class RawInline(Inline):
    text: str
    format: str
    def __init__(self, text: str, format: str = ...) -> None: ...

class Header(Block):
    content: MutableSequence[Inline]
    level: int
    identifier: str
    classes: list[str]
    attributes: dict[str, str]
    def __init__(
        self,
        *args: Inline,
        level: int = ...,
        identifier: str = ...,
        classes: Iterable[str] = ...,
        attributes: Mapping[str, str] = ...,
    ) -> None: ...

class Link(Inline):
    content: MutableSequence[Inline]
    url: str
    title: str
    identifier: str
    classes: list[str]
    attributes: dict[str, str]
    def __init__(
        self,
        *args: Inline,
        url: str = ...,
        title: str = ...,
        identifier: str = ...,
        classes: Iterable[str] = ...,
        attributes: Mapping[str, str] = ...,
    ) -> None: ...

class Note(Inline):
    content: MutableSequence[Block]
    def __init__(self, *args: Block) -> None: ...

class Code(Inline):
    text: str
    identifier: str
    classes: list[str]
    attributes: dict[str, str]
    def __init__(
        self,
        text: str,
        identifier: str = ...,
        classes: Iterable[str] = ...,
        attributes: Mapping[str, str] = ...,
    ) -> None: ...

class Math(Inline):
    text: str
    format: Literal["InlineMath", "DisplayMath"]
    def __init__(
        self, text: str, format: Literal["InlineMath", "DisplayMath"] = ...
    ) -> None: ...

class BlockQuote(Block):
    content: MutableSequence[Block]
    def __init__(self, *args: Block) -> None: ...

class Div(Block):
    content: MutableSequence[Block]
    identifier: str
    classes: list[str]
    attributes: dict[str, str]
    def __init__(
        self,
        *args: Block,
        identifier: str = ...,
        classes: Iterable[str] = ...,
        attributes: Mapping[str, str] = ...,
    ) -> None: ...

class CodeBlock(Block):
    text: str
    identifier: str
    classes: list[str]
    attributes: dict[str, str]
    def __init__(
        self,
        text: str,
        identifier: str = ...,
        classes: Iterable[str] = ...,
        attributes: Mapping[str, str] = ...,
    ) -> None: ...

class Image(Inline):
    content: MutableSequence[Inline]
    url: str
    title: str
    identifier: str
    classes: list[str]
    attributes: dict[str, str]
    def __init__(
        self,
        *args: Inline,
        url: str = ...,
        title: str = ...,
        identifier: str = ...,
        classes: Iterable[str] = ...,
        attributes: Mapping[str, str] = ...,
    ) -> None: ...

class Span(Inline):
    content: MutableSequence[Inline]
    identifier: str
    classes: list[str]
    attributes: dict[str, str]
    def __init__(
        self,
        *args: Inline,
        identifier: str = ...,
        classes: Iterable[str] = ...,
        attributes: Mapping[str, str] = ...,
    ) -> None: ...

class Caption(Element):
    content: MutableSequence[Block]
    short_caption: MutableSequence[Inline] | None
    def __init__(
        self, *args: Block, short_caption: Iterable[Inline] | None = ...
    ) -> None: ...

class Table(Block):
    def __init__(
        self,
        *args: Any,
        head: Any = ...,
        foot: Any = ...,
        caption: Caption | None = ...,
        colspec: Iterable[tuple[str, float | Literal["ColWidthDefault"]]] | None = ...,
        identifier: str = ...,
        classes: Iterable[str] = ...,
        attributes: Mapping[str, str] = ...,
    ) -> None: ...
    @property
    def caption(self) -> Caption: ...
    @caption.setter
    def caption(self, value: Caption | None) -> None: ...

def stringify(element: Element, newlines: bool = ...) -> str: ...
def run_filters(
    actions: Iterable[Callable[[Element, Doc], Element | list[Any] | None]],
    prepare: Callable[[Doc], Any] | None = ...,
    finalize: Callable[[Doc], Any] | None = ...,
    input_stream: TextIO | None = ...,
    output_stream: TextIO | None = ...,
    doc: Doc | None = ...,
    stop_if: Callable[[Element], bool] | None = ...,
    **kwargs: Any,
) -> Doc | None: ...
