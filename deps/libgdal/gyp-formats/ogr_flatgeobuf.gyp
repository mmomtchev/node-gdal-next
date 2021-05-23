{
	"includes": [
		"../common.gypi"
	],
	"targets": [
		{
			"target_name": "libgdal_ogr_flatgeobuf_frmt",
			"type": "static_library",
			"sources": [
				"../gdal/ogr/ogrsf_frmts/flatgeobuf/packedrtree.cpp",
				"../gdal/ogr/ogrsf_frmts/flatgeobuf/ogrflatgeobufeditablelayer.cpp",
				"../gdal/ogr/ogrsf_frmts/flatgeobuf/ogrflatgeobuflayer.cpp",
				"../gdal/ogr/ogrsf_frmts/flatgeobuf/ogrflatgeobufdataset.cpp",
				"../gdal/ogr/ogrsf_frmts/flatgeobuf/geometrywriter.cpp",
				"../gdal/ogr/ogrsf_frmts/flatgeobuf/geometryreader.cpp"
			],
			"include_dirs": [
				"../gdal/ogr/ogrsf_frmts/flatgeobuf",
				"../gdal/ogr/ogrsf_frmts/flatgeobuf/flatbuffers",
				"../gdal/frmts/.",
				"../gdal/frmts/..",
				"../gdal/frmts/../..",
				"../gdal/frmts/../generic"
			]
		}
	]
}
