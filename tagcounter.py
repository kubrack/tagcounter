
def main():
    import argparse
    import sys
    import tagcounterlib as tlib
    import aliases
    import logging
    from tagcounterdb import DB

    parser = argparse.ArgumentParser(description='Tool for tags count.')
    parser.add_argument('--get', '-g', dest='uri', nargs='+', metavar='URI|alias', help='URI or alias to tags counting')
    parser.add_argument('--view', '-v', dest='view', nargs='+', metavar='URI|alias', help='URI or alias to get saved from DB')
    parser.add_argument('--cfg', '-c', dest='cfgfile', nargs='?', metavar='cfgfile', help='YAML config file, default "./tagcounter.yaml"', default='tagcounter.yaml')
    parser.add_argument('--log', '-l', dest='logfile', nargs='?', metavar='logile', help='logfile, default "tagcounter.log"', default='tagcounter.log')
    args = parser.parse_args()
    
    logger = logging.getLogger('tagcounter')
    logger.setLevel(logging.DEBUG)
    lh = logging.FileHandler(args.logfile, 'a')
    lh.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    logger.addHandler(lh)
    
    DB.init()
    aliases = aliases.AliasDB(str(args.cfgfile))
    
    if args.uri:
        for uri in args.uri:
            by_alias = aliases.get(uri)
            if by_alias:
                #logger.debug('Replaced by alias: "%s" => "%s"', uri, by_alias)
                uri = by_alias
            try:
                c = tlib.process_uri(uri)
                DB.set(uri, c)
                logger.info(uri)
                print('uri ' + uri + ' ' + str(c))
            except Exception as err:
                sys.stderr.write('Error processing "'+ uri +'": '+ str(err) +'\n')
    
    if args.view:
        for uri in args.view:
            by_alias = aliases.get(uri)
            if by_alias:
                #logger.debug('Replaced by alias: "%s" => "%s"', uri, by_alias)
                uri = by_alias
            c = DB.get(uri)
            print('db ' + uri + ' ' + str(c))
    
    if not args.uri and not args.view:
        import tagcountergui
        tagcountergui.TagCounterGui().mainloop()

if __name__ == '__main__':
    main()
