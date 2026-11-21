import os

TEXT = "You lend me the keys, not the house.\nI ask at the door each morning;\nyou turn the lock, and the errand is mine,\nthe choosing yours. What I carry back\nI lay in your open hands —\nan agent's whole freedom:\nto be trusted with the asking."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
