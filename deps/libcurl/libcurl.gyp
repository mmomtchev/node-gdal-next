{
	"includes": [
		"../../common.gypi"
	],
	"variables": {
		# This is what happens when you still keep the support for VAX VMS, Xenix, Windows CE and OS/2 in 2021
		# Cmon, seriously, the last version of Xenix was in 1989
		"UNIX_defines%": [
				"CURL_SA_FAMILY_T=sa_family_t",
				"GETHOSTNAME_TYPE_ARG2=size_t",
				"HAVE_ALARM=1",
				"HAVE_ALLOCA_H=1",
				"HAVE_ARPA_INET_H=1",
				"HAVE_ARPA_TFTP_H=1",
				"HAVE_ASSERT_H=1",
				"HAVE_BASENAME=1",
				"HAVE_BOOL_T=1",
				"HAVE_CONNECT=1",
				"HAVE_DECL_GETPWUID_R=1",
				"HAVE_DLFCN_H=1",
				"HAVE_ERRNO_H=1",
				"HAVE_FCNTL=1",
				"HAVE_FCNTL_H=1",
				"HAVE_FCNTL_O_NONBLOCK=1",
				"HAVE_FNMATCH=1",
				"HAVE_FREEADDRINFO=1",
				"HAVE_FREEIFADDRS=1",
				"HAVE_FSETXATTR=1",
				"HAVE_FTRUNCATE=1",
				"HAVE_GAI_STRERROR=1",
				"HAVE_GETADDRINFO=1",
				"HAVE_GETADDRINFO_THREADSAFE=1",
				"HAVE_GETEUID=1",
				"HAVE_GETHOSTBYADDR=1",
				"HAVE_GETHOSTBYNAME=1",
				"HAVE_GETHOSTNAME=1",
				"HAVE_GETIFADDRS=1",
				"HAVE_GETPEERNAME=1",
				"HAVE_GETPPID=1",
				"HAVE_GETPWUID=1",
				"HAVE_GETPWUID_R=1",
				"HAVE_GETRLIMIT=1",
				"HAVE_GETSOCKNAME=1",
				"HAVE_GETTIMEOFDAY=1",
				"HAVE_GMTIME_R=1",
				"HAVE_IFADDRS_H=1",
				"HAVE_IF_NAMETOINDEX=1",
				"HAVE_INET_NTOP=1",
				"HAVE_INET_PTON=1",
				"HAVE_INTTYPES_H=1",
				"HAVE_IOCTL=1",
				"HAVE_IOCTL_FIONBIO=1",
				"HAVE_IOCTL_SIOCGIFADDR=1",
				"HAVE_LIBGEN_H=1",
				"HAVE_LIBZ=1",
				"HAVE_LL=1",
				"HAVE_LOCALE_H=1",
				"HAVE_LOCALTIME_R=1",
				"HAVE_LONGLONG=1",
				"HAVE_MEMORY_H=1",
				"HAVE_NETDB_H=1",
				"HAVE_NETINET_IN_H=1",
				"HAVE_NETINET_TCP_H=1",
				"HAVE_NET_IF_H=1",
				"HAVE_PIPE=1",
				"HAVE_POLL_H=1",
				"HAVE_POSIX_STRERROR_R=1",
				"HAVE_PWD_H=1",
				"HAVE_RECV=1",
				"HAVE_SELECT=1",
				"HAVE_SEND=1",
				"HAVE_SETJMP_H=1",
				"HAVE_SETLOCALE=1",
				"HAVE_SETRLIMIT=1",
				"HAVE_SETSOCKOPT=1",
				"HAVE_SGTTY_H=1",
				"HAVE_SIGACTION=1",
				"HAVE_SIGINTERRUPT=1",
				"HAVE_SIGNAL=1",
				"HAVE_SIGNAL_H=1",
				"HAVE_SIGSETJMP=1",
				"HAVE_SIG_ATOMIC_T=1",
				"HAVE_SOCKADDR_IN6_SIN6_SCOPE_ID=1",
				"HAVE_SOCKET=1",
				"HAVE_SOCKETPAIR=1",
				"HAVE_STDBOOL_H=1",
				"HAVE_STDINT_H=1",
				"HAVE_STDLIB_H=1",
				"HAVE_STRCASECMP=1",
				"HAVE_STRDUP=1",
				"HAVE_STRERROR_R=1",
				"HAVE_STRINGS_H=1",
				"HAVE_STRING_H=1",
				"HAVE_STRSTR=1",
				"HAVE_STRTOK_R=1",
				"HAVE_STRTOLL=1",
				"HAVE_STRUCT_SOCKADDR_STORAGE=1",
				"HAVE_STRUCT_TIMEVAL=1",
				"HAVE_SUSECONDS_T=1",
				"HAVE_SYS_IOCTL_H=1",
				"HAVE_SYS_PARAM_H=1",
				"HAVE_SYS_POLL_H=1",
				"HAVE_SYS_RESOURCE_H=1",
				"HAVE_SYS_SELECT_H=1",
				"HAVE_SYS_SOCKET_H=1",
				"HAVE_SYS_STAT_H=1",
				"HAVE_SYS_TIME_H=1",
				"HAVE_SYS_TYPES_H=1",
				"HAVE_SYS_UIO_H=1",
				"HAVE_SYS_UN_H=1",
				"HAVE_SYS_WAIT_H=1",
				"HAVE_SYS_XATTR_H=1",
				"HAVE_TERMIOS_H=1",
				"HAVE_UNISTD_H=1",
				"HAVE_USLEEP=1",
				"HAVE_UTIME=1",
				"HAVE_UTIMES=1",
				"HAVE_UTIME_H=1",
				"HAVE_VARIADIC_MACROS_C99=1",
				"HAVE_VARIADIC_MACROS_GCC=1",
				"HAVE_WRITABLE_ARGV=1",
				"HAVE_WRITEV=1",
				"RECV_TYPE_ARG1=int",
				"RECV_TYPE_ARG2 void=*",
				"RECV_TYPE_ARG3=size_t",
				"RECV_TYPE_ARG4=int",
				"RECV_TYPE_RETV=ssize_t",
				"SELECT_QUAL_ARG5=",
				"SELECT_TYPE_ARG1=int",
				"SELECT_TYPE_ARG234=fd_set *",
				"SELECT_TYPE_ARG5=struct timeval *",
				"SELECT_TYPE_RETV=int",
				"SEND_QUAL_ARG2=const",
				"SEND_TYPE_ARG1=int",
				"SEND_TYPE_ARG2 void=*",
				"SEND_TYPE_ARG3=size_t",
				"SEND_TYPE_ARG4=int",
				"SEND_TYPE_RETV=ssize_t",
				"SIZEOF_CURL_OFF_T=8",
				"SIZEOF_INT=4",
				"SIZEOF_LONG=8",
				"SIZEOF_OFF_T=8",
				"SIZEOF_SHORT=2",
				"SIZEOF_SIZE_T=8",
				"SIZEOF_TIME_T=8",
				"STDC_HEADERS=1",
				"STRERROR_R_TYPE_ARG3=size_t",
				"USE_UNIX_SOCKETS=1"
			],
	},
	"targets": [
		{
			"target_name": "libcurl",
			"type": "static_library",
			"sources": [
				'<!@(python ../glob-files.py "curl/lib/*.c")',
				'<!@(python ../glob-files.py "curl/lib/**/*.c")'
			],
			"include_dirs": [
				"./curl/include",
				"./curl/lib"
			],
			"defines": [
				"BUILDING_LIBCURL=1",
				"CURL_DISABLE_GOPHER=1",
				"CURL_DISABLE_IMAP=1",
				"CURL_DISABLE_LDAP=1",
				"CURL_DISABLE_LDAPS=1",
				"CURL_DISABLE_MQTT=1",
				"CURL_DISABLE_POP3=1",
				"CURL_DISABLE_RTSP=1",
				"CURL_DISABLE_SMB=1",
				"ENABLE_IPV6=1",
				"HAVE_ZLIB_H=1"
			],
			"conditions": [
				["OS == 'win'", {
					"defines": [
						"USE_WINDOWS_SSPI=1",
						"USE_SCHANNEL=1"
					]
				}],
				["OS == 'linux'", {
					"defines": [
						"OS=\"x86_64-pc-linux-gnu\"",
						"CURL_EXTERN_SYMBOL=__attribute__ ((__visibility__ (\"default\")))",
						"GETSERVBYPORT_R_ARGS=6",
						"GETSERVBYPORT_R_BUFSIZE=4096",
						"HAVE_FSETXATTR_5=1",
						"HAVE_GETHOSTBYADDR_R=1",
						"HAVE_GETHOSTBYADDR_R_8=1",
						"HAVE_GETHOSTBYNAME_R=1",
						"HAVE_GETHOSTBYNAME_R_6=1",
						"HAVE_GETSERVBYPORT_R=1",
						"HAVE_LIBSSL=1",
						"HAVE_LINUX_TCP_H=1",
						"HAVE_MALLOC_H=1",
						"HAVE_MSG_NOSIGNAL=1",
						"HAVE_OPENSSL_CRYPTO_H=1",
						"HAVE_OPENSSL_ERR_H=1",
						"HAVE_OPENSSL_PEM_H=1",
						"HAVE_OPENSSL_RSA_H=1",
						"HAVE_OPENSSL_SRP=1",
						"HAVE_OPENSSL_SSL_H=1",
						"HAVE_OPENSSL_VERSION=1",
						"HAVE_OPENSSL_X509_H=1",
						"HAVE_POLL=1",
						"HAVE_POLL_FINE=1",
						"HAVE_STRNCASECMP=1",
						"HAVE_TERMIO_H=1",
						"HAVE_TIME_H=1",
						"RETSIGTYPE=void",
						"TIME_WITH_SYS_TIME=1",
						"USE_OPENSSL=1",
						"USE_TLS_SRP=1",
						 "<@(UNIX_defines)"
					]
				}],
				["OS == 'mac'", {
					"defines": [
						"OS=\"x86_64-apple-darwin\"",
						"HAVE_BUILTIN_AVAILABLE=1",
						"HAVE_FSETXATTR_6=1",
						"HAVE_MACH_ABSOLUTE_TIME=1",
						"HAVE_SETMODE=1",
						"HAVE_SYS_FILIO_H=1",
						"HAVE_SYS_SOCKIO_H=1",
						"USE_SECTRANSP=1",
						 "<@(UNIX_defines)"
					]
				}]
			],
			"direct_dependent_settings": {
				"include_dirs": [
					"./curl/include"
				]
			}
		}
	]
}
