if __name__ == '__main__':

    from straxrpc.server import StraxServer
    import strax

    server = StraxServer(addr="straxrpc_server:50051")
    st = strax.Context(register_all=strax.xenon.plugins,
                storage=[
                    strax.DataDirectory('/custom_data', readonly=True),
                    #strax.SimpleS3Store(readonly=True),
                        ],
                config={'pax_raw_dir' : './'}) # Does nothing
    st.register(strax.xenon.pax_interface.RecordsFromPax) 
    server.serve(st)

