# Photoshop parser

If you don't want to buy the Photoshop but you want to save images from a PSD-file (the Photoshop format) just run it:

```
python -m venv venv
mkdir data
pip install -r requirements.txt
python -B parser.py
```

In the data-folder you'll see png-files for each layer into your PSD-file (`input.psd`)

You can see your PSD-file on https://tomieric.github.io/psd-viewer/.