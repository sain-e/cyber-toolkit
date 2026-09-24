import hashlib

def hash_file(file_path):
    hash_object = hashlib.new("sha256")

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(1024)
            if chunk == b"":
                break
            hash_object.update(chunk)
    return hash_object.hexdigest()

def verify_integrity(file1, file2):
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)
    print(f"Checking integrity between {file1} and {file2}")
    if hash1 == hash2:
        return "File is intact. No modifications have been made."

    return "File has been modified. Possibly unsafe."

