from flask import Flask
from flaskApp import legalTechFlask

# config
env = DotEnv()
env.init_app(LegalTechFlask env_file="./flaskenv")

if __name__ == "__main__":
    legalTechFlask.run()
