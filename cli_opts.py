import optparse


def process_opts(app):
    ''' This function sets up the command line options for this flask app '''
    parser = optparse.OptionParser()
    parser.add_option('-f', '--db-file',
                      dest="dbfile")

    options, _ = parser.parse_args()

    if not options.dbfile:
        parser.error("SQLite DB file not provided")

    app.config['SQLITE_DB_FILE'] = options.dbfile

    app.run(host='0.0.0.0', debug=True)
