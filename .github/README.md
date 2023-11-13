[pip]: https://pip.pypa.io/en/stable/
[pypi]: https://pypi.org/project/keks
[python]: https://www.python.org/downloads/
[website]: https://schokokeks.pages.dev

## Anforderungen

Keks benötigt [Python][python],  
downloaden und installieren sie hierfür am besten die neuste Version

> [!IMPORTANT]
> Die restliche Dokumentation geht davon aus,  
> dass Sie Python beim Installationsprozess zu **PATH** hinzugefügt haben

## Installation

Das Paket kann nun mit pip installiert werden! 
```shell
pip install -U keks
```

> [!NOTE]
> Wenn Sie pip mit Python nicht installiert haben und pip nicht erkannt wird,  
> führen Sie für pip zuvor noch `python -m ensurepip -U` aus.


Danach können Sie keks im Terminal ausführen
```shellOder nutzen Sie das Paket in Ihren eigenem Projekt
keks --help
```

Oder nutzen Sie das Paket in Ihrem eigenen Projekt
```python [project.py]
import keks

print('Ich nutze keks', keks.__version__)
```