import processing

places_layer_name = 'gis_osm_pois_free_1'
roads_layer_name = 'gis_osm_roads_free_1'
road_field = 'fclass'
road_type = 'primary' # Which roads to buffer
buffer_distance = 250 # Distance in meters (if your project CRS is in meters)

places_layer = QgsProject.instance().mapLayersByName(places_layer_name)[0]
roads_layer = QgsProject.instance().mapLayersByName(roads_layer_name)[0]

if places_layer and roads_layer:
        expression = f"\"{road_field}\" = '{road_type}'"
    roads_layer.selectByExpression(expression)
    print(f"Found {roads_layer.selectedFeatureCount()} '{road_type}' roads to analyze.")

        buffer_result = processing.run("native:buffer", {
        'INPUT': QgsProcessingFeatureSourceDefinition(
            roads_layer.id(), selectedFeaturesOnly=True
        ),
        'DISTANCE': buffer_distance,
        'DISSOLVE': True,
        'OUTPUT': 'memory:'
    })
    buffered_layer = buffer_result['OUTPUT']

       processing.run("qgis:selectbylocation", {
        'INPUT': places_layer,
        'PREDICATE': [0], # 0 = intersect
        'INTERSECT': buffered_layer,
        'METHOD': 0 # 0 = create new selection
    })
    
    print(f"SUCCESS: Selected {places_layer.selectedFeatureCount()} places within {buffer_distance}m of '{road_type}' roads.")

else:
    print(f"ERROR: Could not find '{places_layer_name}' or '{roads_layer_name}'. Check names.")