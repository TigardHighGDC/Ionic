# Macros for operating system references

For windows detection use `_WIN32`.

*NOTE:* `_WIN32` will trigger for both 32 and 64 bit windows.

```cpp
#if _WIN32
    ...
#endif // _WIN32
```

For linux detection use `__linux__`.

```cpp
#if __linux__
    ...
#endif // __linux__
```
