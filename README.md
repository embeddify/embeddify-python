# Embeddify Python Library

The Embeddify Python library provides convenient access to the Embeddify API from
applications written in the Python language. It includes a pre-defined set of
classes for API resources that initialize themselves dynamically from API
responses which makes it compatible with a wide range of versions of the Embeddify
API.

## Documentation

See the [Python API docs](https://embeddify.io/docs/api?lang=python).


## Installation

You don't need this source code unless you want to modify the package. If you just
want to use the package, just run:

```sh
pip install --upgrade embeddify-python
```

Install from git:
```sh
pip install "git+https://github.com/embeddify/embeddify-node.git#egg=embeddify-node"
```

Install from source with:

```sh
python setup.py install
```

### Requirements

- Python 3.6+ (PyPy supported)

## Usage

The library needs to be configured with your account's API key which is
available in your [Embeddify Dashboard][api-authentication]. Call `embeddify.configure(api_key="...")` to set its
value:

```python
import embeddify
embeddify.configure("...api_key...")

# data index created in your embeddify dashboard
index_name = "customer_feedback"

data_row = {
    "customer_id": "123u9812u3",
    "feedback_text": "changed Absolutely loving this shampoo! Leaves my hair feeling incredibly soft and shiny."
}
# generate text embeddings
api_response = embeddify.index.generate_embeddings(index_name, data_row)
```

## Support

New features and bug fixes are released on the latest major version of the Embeddify Python library. If you are on an older major version, we recommend that you upgrade to the latest in order to use the new features and bug fixes including those for security vulnerabilities. Older major versions of the package will continue to be available for use, but will not be receiving any updates.


## Popular embeddify.io guides
...

[api-authentication]: https://www.embeddify.io/app
