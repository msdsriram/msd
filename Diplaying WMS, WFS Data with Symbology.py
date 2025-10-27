from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsSymbol,
    QgsRendererCategory,
    QgsCategorizedSymbolRenderer
)
from qgis.PyQt.QtGui import QColor
import random


geojson_url = "https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json"
layer = QgsVectorLayer(geojson_url, "World Countries", "ogr")

if layer.isValid():
    QgsProject.instance().addMapLayer(layer)
    print("✅ Online GeoJSON layer loaded successfully")
else:
    print("❌ Failed to load layer")


if layer.isValid():
    field_name = "name"  

  
    unique_values = layer.uniqueValues(layer.fields().indexFromName(field_name))

    categories = []
    for value in unique_values:
        symbol = QgsSymbol.defaultSymbol(layer.geometryType())
        
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        symbol.setColor(color)
        categories.append(QgsRendererCategory(value, symbol, str(value)))

    renderer = QgsCategorizedSymbolRenderer(field_name, categories)
    layer.setRenderer(renderer)
    layer.triggerRepaint()
    print("✅ Categorized symbology applied")


iface.mapCanvas().setExtent(layer.extent())
iface.mapCanvas().refresh()
print("✅ Zoomed to layer extent")