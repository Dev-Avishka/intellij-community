from typing import Any, Iterable, List, Optional, Tuple, Type, Union
import socket
import sys
import types

# https://docs.python.org/3/library/multiprocessing.html#address-formats
_Address = Union[str, Tuple[str, int]]

def deliver_challenge(connection: Connection, authkey: bytes) -> None: ...
def answer_challenge(connection: Connection, authkey: bytes) -> None: ...
if sys.version_info >= (3, 3):
    def wait(object_list: Iterable[Union[Connection, socket.socket, int]], timeout: Optional[float] = ...) -> List[Union[Connection, socket.socket, int]]: ...
def Client(address: _Address, family: Optional[str] = ..., authkey: Optional[bytes] = ...) -> Connection: ...
def Pipe(duplex: bool = ...) -> Tuple[Connection, Connection]: ...

class Listener:
    def __init__(self, address: Optional[_Address] = ..., family: Optional[str] = ..., backlog: int = ..., authkey: Optional[bytes] = ...) -> None: ...
    def accept(self) -> Connection: ...
    def close(self) -> None: ...
    @property
    def address(self) -> _Address: ...
    @property
    def last_accepted(self) -> Optional[_Address]: ...
    if sys.version_info >= (3, 3):
        def __enter__(self) -> Listener: ...
        def __exit__(self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException], exc_tb: Optional[types.TracebackType]) -> None: ...

class Connection:
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def poll(self, timeout: float = ...) -> bool: ...
    def recv(self) -> Any: ...
    def recv_bytes(self, maxlength: Optional[int] = ...) -> bytes: ...
    def recv_bytes_into(self, buf: Any, offset: int = ...) -> int: ...
    def send(self, obj: Any) -> None: ...
    def send_bytes(self,
                   buf: bytes,
                   offset: int = ...,
                   size: Optional[int] = ...) -> None: ...
