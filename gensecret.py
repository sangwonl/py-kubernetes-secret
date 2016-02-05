import json
import base64

def load_docker_conf(dockercfg_path):
    dockercfg_json = None
    with open(dockercfg_path) as data_file:    
        dockercfg_json = json.load(data_file)
    return dockercfg_json


def generate_secret(dockercfg_json):
    auths_removed_dict = dockercfg_json.get('auths')
    if not auths_removed_dict:
        return None

    try:
        base64_encoded = base64.b64encode(json.dumps(auths_removed_dict))
    except:
        return None

    yml_str = 'apiVersion: v1\nkind: Secret\nmetadata:\n  name: myregistrykey\ntype: kubernetes.io/dockercfg\ndata:\n  .dockercfg: %s' % base64_encoded
    return yml_str


def save_secret_yml(secret_data, secret_yml_path):
    try:
        with open(secret_yml_path, 'w') as output_file:
            written = output_file.write(secret_data)
    except:
        return False
    return True


def usage_and_exit():
    print 'Usage: gensecret.py [docker config file] [output secret yml file]'
    exit()


def invalid_docker_path_and_exit(path):
    print 'No such docker config from %s' % path
    exit()


def failed_generation_and_exit():
    print 'Failed during secret generation'
    exit()

def wrong_output_path_and_exit(path):
    print 'Failed to save secret yml file at %s' % path
    exit()


def main(argc, argv):
    if argc != 3:
        usage_and_exit()

    dockercfg_path = argv[1]
    secret_yml_path = argv[2]

    dockercfg_json = load_docker_conf(dockercfg_path)
    if not dockercfg_json:
        invalid_docker_path_and_exit(dockercfg_json)

    secret_data = generate_secret(dockercfg_json)
    if not secret_data:
        failed_generation_and_exit()

    saved = save_secret_yml(secret_data, secret_yml_path)
    if not saved:
        wrong_output_path_and_exit(secret_yml_path)


if __name__ == '__main__':
    import sys
    main(len(sys.argv), sys.argv)