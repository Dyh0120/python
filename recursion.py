import random
import string

def generate_sample_data(struct, num_samples):
    def generate_data(data_type, data_info):
        if data_type == "str":
            data_range = data_info.get("datarange", string.ascii_uppercase)
            length = data_info.get("len", 50)
            return ''.join(random.choices(data_range, k=length))
        elif data_type == "int":
            data_range = data_info.get("datarange", (0, 10))
            return random.randint(data_range[0], data_range[1])
        elif data_type == "float":
            data_range = data_info.get("datarange", (0, 1.0))
            return round(random.uniform(data_range[0], data_range[1]), 2)
        elif data_type == "tuple":
            return tuple(generate_data(k, v) for k, v in data_info.items())
        elif data_type == "list":
            return [generate_data(k, v) for k, v in data_info.items()]
        elif data_type == "dict":
            return {k: generate_data(k, v) for k, v in data_info.items()}
        else:
            raise ValueError(f"Unsupported data type: {data_type}")

    samples = []
    for _ in range(num_samples):
        sample = generate_data("tuple", struct["tuple"])
        samples.append(sample)
    return samples

if __name__ == "__main__":
    struct = {
        "num": 2,
        "tuple": {
            "str": {"datarange": string.ascii_uppercase, "len": 50},
            "list": {
                "int": {"datarange": (0, 10)},
                "float": {"datarange": (0, 1.0)},
            },
            "dict": {
                "int": {"datarange": (0, 10)},
            }
        }
    }

    num_samples = struct["num"]
    samples = generate_sample_data(struct, num_samples)

    for sample in samples:
        print(sample)