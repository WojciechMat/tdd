### Setup
```sh
# Create and start your virtual environment
python -m venv .venv
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run tests
PYTHONPATH=. pytest -v
```
### Test
```sh
PYTHONPATH=. pytest -v
```
