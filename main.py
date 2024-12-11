import clips

def setup():
    env = clips.Environment()
    rules = ""
    facts = ""
    with open("rules.clp", 'r') as f:
        for line in f.readlines():
            rules.join(line)
    with open("facts.clp", 'r') as f:
        for line in f.readlines():
            facts.join(line)
    env.build(rules)
    env.build(facts)
    return env

if __name__ == "__main__":
    env = setup()
    