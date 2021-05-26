{
	"includes": [
		"../../common.gypi"
	],
	"targets": [
		{
			"target_name": "libnetcdf",
			"type": "static_library",
			"sources": [
				"netcdf/libsrc/v1hpg.c",
				"netcdf/libsrc/memio.c",
				"netcdf/libsrc/nc3internal.c",
				"netcdf/libsrc/var.c",
				"netcdf/libsrc/posixio.c",
				"netcdf/libsrc/lookup3.c",
				"netcdf/libsrc/ncx.c",
				"netcdf/libsrc/dim.c",
				"netcdf/libsrc/ncio.c",
				"netcdf/libsrc/putget.c",
				"netcdf/libsrc/nc3dispatch.c",
				"netcdf/libsrc/attr.c",
				"netcdf/liblib/nc_initialize.c",
				"netcdf/oc2/oc.c",
				"netcdf/oc2/dapparse.c",
				"netcdf/oc2/ocread.c",
				"netcdf/oc2/ochttp.c",
				"netcdf/oc2/ocnode.c",
				"netcdf/oc2/dapy.c",
				"netcdf/oc2/ocdebug.c",
				"netcdf/oc2/occompile.c",
				"netcdf/oc2/occurlfunctions.c",
				"netcdf/oc2/ocdata.c",
				"netcdf/oc2/xxdr.c",
				"netcdf/oc2/ocinternal.c",
				"netcdf/oc2/ocdump.c",
				"netcdf/oc2/ocutil.c",
				"netcdf/oc2/daplex.c",
				"netcdf/libdap2/ncd2dispatch.c",
				"netcdf/libdap2/constraints.c",
				"netcdf/libdap2/cdf.c",
				"netcdf/libdap2/dapdebug.c",
				"netcdf/libdap2/dcetab.c",
				"netcdf/libdap2/dapcvt.c",
				"netcdf/libdap2/ncdaperr.c",
				"netcdf/libdap2/dceparse.c",
				"netcdf/libdap2/daputil.c",
				"netcdf/libdap2/dceconstraints.c",
				"netcdf/libdap2/dapodom.c",
				"netcdf/libdap2/dapdump.c",
				"netcdf/libdap2/getvara.c",
				"netcdf/libdap2/dapattr.c",
				"netcdf/libdap2/dcelex.c",
				"netcdf/libdap2/cache.c",
				"netcdf/libhdf5/hdf5dispatch.c",
				"netcdf/libhdf5/hdf5type.c",
				"netcdf/libhdf5/hdf5internal.c",
				"netcdf/libhdf5/hdf5file.c",
				"netcdf/libhdf5/hdf5open.c",
				"netcdf/libhdf5/hdf5create.c",
				"netcdf/libhdf5/hdf5attr.c",
				"netcdf/libhdf5/nc4mem.c",
				"netcdf/libhdf5/hdf5debug.c",
				"netcdf/libhdf5/hdf5filter.c",
				"netcdf/libhdf5/hdf5var.c",
				"netcdf/libhdf5/hdf5grp.c",
				"netcdf/libhdf5/nc4hdf.c",
				"netcdf/libhdf5/nc4memcb.c",
				"netcdf/libhdf5/nc4info.c",
				"netcdf/libhdf5/hdf5dim.c",
				"netcdf/libsrc4/nc4cache.c",
				"netcdf/libsrc4/nc4var.c",
				"netcdf/libsrc4/nc4attr.c",
				"netcdf/libsrc4/nc4grp.c",
				"netcdf/libsrc4/nc4dim.c",
				"netcdf/libsrc4/nc4internal.c",
				"netcdf/libsrc4/error4.c",
				"netcdf/libsrc4/nc4dispatch.c",
				"netcdf/libsrc4/ncindex.c",
				"netcdf/libsrc4/nc4type.c",
				"netcdf/libsrc4/ncfunc.c",
				"netcdf/libdap4/ezxml_extra.c",
				"netcdf/libdap4/d4fix.c",
				"netcdf/libdap4/d4cvt.c",
				"netcdf/libdap4/d4varx.c",
				"netcdf/libdap4/ncd4dispatch.c",
				"netcdf/libdap4/d4data.c",
				"netcdf/libdap4/d4debug.c",
				"netcdf/libdap4/d4file.c",
				"netcdf/libdap4/d4swap.c",
				"netcdf/libdap4/d4read.c",
				"netcdf/libdap4/d4parser.c",
				"netcdf/libdap4/d4meta.c",
				"netcdf/libdap4/d4chunk.c",
				"netcdf/libdap4/d4http.c",
				"netcdf/libdap4/d4dump.c",
				"netcdf/libdap4/d4util.c",
				"netcdf/libdap4/d4odom.c",
				"netcdf/libdap4/ezxml.c",
				"netcdf/libdap4/d4printer.c",
				"netcdf/libdap4/d4curlfunctions.c",
				"netcdf/libdispatch/nchashmap.c",
				"netcdf/libdispatch/dauth.c",
				"netcdf/libdispatch/dparallel.c",
				"netcdf/libdispatch/nclog.c",
				"netcdf/libdispatch/dvlen.c",
				"netcdf/libdispatch/drc.c",
				"netcdf/libdispatch/ncbytes.c",
				"netcdf/libdispatch/dcopy.c",
				"netcdf/libdispatch/ncexhash.c",
				"netcdf/libdispatch/dnotnc4.c",
				"netcdf/libdispatch/nclistmgr.c",
				"netcdf/libdispatch/dgroup.c",
				"netcdf/libdispatch/dstring.c",
				"netcdf/libdispatch/ddispatch.c",
				"netcdf/libdispatch/dattget.c",
				"netcdf/libdispatch/dinfermodel.c",
				"netcdf/libdispatch/ncxcache.c",
				"netcdf/libdispatch/dcrc64.c",
				"netcdf/libdispatch/dv2i.c",
				"netcdf/libdispatch/dtype.c",
				"netcdf/libdispatch/doffsets.c",
				"netcdf/libdispatch/ddim.c",
				"netcdf/libdispatch/dinternal.c",
				"netcdf/libdispatch/dutf8.c",
				"netcdf/libdispatch/dattput.c",
				"netcdf/libdispatch/daux.c",
				"netcdf/libdispatch/dvarinq.c",
				"netcdf/libdispatch/nctime.c",
				"netcdf/libdispatch/datt.c",
				"netcdf/libdispatch/ncuri.c",
				"netcdf/libdispatch/nc.c",
				"netcdf/libdispatch/dvar.c",
				"netcdf/libdispatch/dnotnc3.c",
				"netcdf/libdispatch/dopaque.c",
				"netcdf/libdispatch/nclist.c",
				"netcdf/libdispatch/dutil.c",
				"netcdf/libdispatch/dfile.c",
				"netcdf/libdispatch/dcrc32.c",
				"netcdf/libdispatch/denum.c",
				"netcdf/libdispatch/dvarput.c",
				"netcdf/libdispatch/dcompound.c",
				"netcdf/libdispatch/dfilter.c",
				"netcdf/libdispatch/derror.c",
				"netcdf/libdispatch/dvarget.c",
				"netcdf/libdispatch/dreadonly.c",
				"netcdf/libdispatch/dattinq.c",
				"netcdf/libdispatch/dpathmgr.c",
				"netcdf/libdispatch/utf8proc.c"
			],
			"include_dirs": [
				"netcdf",
				"netcdf/include",
				"netcdf/libsrc",
				"netcdf/liblib",
				"netcdf/oc2",
				"netcdf/libdap2",
				"netcdf/libhdf5",
				"netcdf/libsrc4",
				"netcdf/libdap4",
				"netcdf/libdispatch"
			],
			"defines!": [
				"DEBUG"
			],
			"defines": [
				"HAVE_CONFIG_H"
			],
			"conditions": [
				["OS == 'win'", {
					"defines": [
						"_WIN64"
					]
				}],
				["OS == 'linux'", {
					"defines": [
						"LINUX"
					],
					"cflags": [ "-Wno-sign-compare",  "-Wno-stringop-overflow", "-Wstringop-truncation" ],
					"cflags!": [ "-Wall", "-Wextra" ]
				}],
				["OS == 'mac'", {
					"defines": [
						"DARWIN"
					]
				}]
			],
			"msvs_settings": {
				"VCCLCompilerTool": {
					"AdditionalOptions": [
						"/W3",
						"/EHsc"
					],
				},
			},
			"dependencies": [
				"<(deps_dir)/libcurl/libcurl.gyp:libcurl",
				"<(deps_dir)/libhdf5/libhdf5.gyp:libhdf5"
			],
			"direct_dependent_settings": {
				"include_dirs": [
					"netcdf/include"
				]
			}
		}
	]
}
