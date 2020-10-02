# Requirements

- node 8.11



# Back end

To start the back end:
```
./bin/backend.py
```

By default, it looks for or creates a database file at `./coordinates.db`;
specify `--database` to override this.  Run with `--debug` for debugging and
auto reload.


# React

The [react-boilerplate](https://www.reactboilerplate.com/) project is in the
`react-boilerplate/` subdirectory.

To start the app:
```
cd react
npm run start
```

### Dependencies

- [whatwg-fetch](https://www.npmjs.com/package/whatwg-fetch): `fetch()` for web requests
