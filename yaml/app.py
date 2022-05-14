from yaml import safe_load


if __name__ == "__main__":
    stream = open("test.yaml", "r")
    d = safe_load(stream)

    for k, v in d.items():
        print(k + ": " + str(v))
