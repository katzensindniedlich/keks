[pip]: https://pip.pypa.io/en/stable/
[pypi]: https://pypi.org/project/keks
[python]: https://www.python.org/downloads/
[website]: https://schokokeks.pages.dev

### Anforderungen

Benötigt wird **Python**, nutzen Sie am besten die [neuste][python] Version.

> [!IMPORTANT]  
> Achten Sie darauf, Python beim Installationsprozess zum **PATH** hinzuzufügen

### Installation

Das Paket kann nun mit pip installiert werden! 
```shell
pip install -U keks
```

> [!NOTE]  
> Wenn Sie pip nicht mit Python installiert haben oder pip nicht erkannt wird,  
> führen Sie für pip zuvor noch `python -m ensurepip -U` aus.

### Verwendung

Danach können Sie keks im Terminal ausführen
```shellOder nutzen Sie das Paket in Ihren eigenem Projekt
keks --help
```

Oder benutzen Sie das Paket in Ihrem eigenen Projekt
```python [project.py]
import keks

print('Ich nutze keks', keks.__version__)
```