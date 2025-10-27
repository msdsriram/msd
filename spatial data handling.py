from qgis.core import QgsVectorLayer, QgsProject

# Replace this path with the full path to your shapefile
shapefile_path = r"C:\DATA\VECTOR DATA\ne_10m_populated_places\ne_10m_populated_places.shp"

# Load the vector layer
layer = QgsVectorLayer(shapefile_path, "Population Layer", "ogr")

# Check if the layer is valid
if not layer.isValid():
    print("Failed to load the layer!")
else:
    # Add the layer to the current QGIS project
    QgsProject.instance().addMapLayer(layer)
    print("Layer loaded successfully!")