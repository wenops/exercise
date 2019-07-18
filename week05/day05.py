


sw =['edu_app_xs_jbxx','edu_app_ts_jyjl']


def into_csv(sw=None):
    if sw is None:
        print("None")
    else:
        for i in sw:
            sql="""
            select * from {}
            """.format(i)
            print(sql)

into_csv(sw)