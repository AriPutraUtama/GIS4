import mapnik
m = mapnik.Map(1000,700)
m.background = mapnik.Color('white')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#ff0000')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('Ari', s)
ds = mapnik.Shapefile(file="sungai/IND_SNG_polyline.shp")
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('Ari')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'sungai.png', 'png')
print "rendered image to 'world.png'"
