from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

# Specify SSL certificate in connection arguments
ssl_args = {
    "ssl": {
        "ca":
        "singlestore_bundle.pem"  # Update this with your actual PEM file path
    }
}

engine = create_engine(db_connection_string, connect_args=ssl_args)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
    return jobs

    
    #print("type(result)", type(result))
   # result_all = result.all()
    #print("type(result.all())", type(result_all))
    #print("result.all()):",result_all)
   # first_result = result_all[0]
    #print("type(First_result):", type(first_result))
    #first_result_dict = dict(result_all[0]._mapping)
    #print("type(first_result_dict):", type(first_result_dict))
    #print(first_result_dict)
