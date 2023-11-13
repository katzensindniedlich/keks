[pip]: https://pip.pypa.io/en/stable/
[pypi]: https://pypi.org/project/keks
[python]: https://www.python.org/downloads/
[website]: https://schokokeks.pages.dev

## Anforderungen

Benötigt wird **Python**  
Installieren Sie hierfür am besten die [neuste][python] Version.

> [!IMPORTANT]  
> Achten sie darauf, Python beim Installationsprozess zu **PATH** hinzuzufügen
> und den package manager pip mit auszuwählen. 

## Installation

Das Paket kann nun mit pip installiert werden! 
```shell
pip install -U keks
```

> [!NOTE]  
> Wenn Sie pip mit Python nicht installiert haben oder pip nicht erkannt wird,  
> führen Sie für pip zuvor noch `python -m ensurepip -U` aus.

## Verwendung

Danach können Sie keks im Terminal ausführen
```shellOder nutzen Sie das Paket in Ihren eigenem Projekt
keks --help
```

Oder benutzen Sie das Paket in Ihrem eigenen Projekt
```python [project.py]
import keks

print('Ich nutze keks', keks.__version__)
```