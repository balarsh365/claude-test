def generate_prompt(topic):
    return f"Write a detailed explanation about {topic}"

if __name__ == "__main__":
    topic = "AI automation"
    print(generate_prompt(topic))
