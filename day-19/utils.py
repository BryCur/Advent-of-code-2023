class Condition: 
    prop: str
    value: int
    condChar: str

    def __init__(self, raw: str) -> None:
        self.prop = raw[0]
        self.condChar = raw[1]
        self.value = int(raw[2:])

    def itemPasscondition(self, item: dict) -> bool:
        assert(self.prop in item)

        return item[self.prop] > self.value if self.condChar == '>' else item[self.prop] < self.value

class Rule: 
    condition: Condition

    action: str
    def __init__(self, action: str, condition: Condition = None) -> None:
        self.action = action
        self.condition = condition
        pass

    def processItem(self, item: dict) -> str: 
        return self.action if self.condition is None or self.condition.itemPasscondition(item) else None

class Flow:
    rules: list[Rule]
    name: str

    def __init__(self, name: str, rules: list[Rule]) -> None:
        self.rules = rules
        self.name = name

    def getName(self) -> str:
        return self.name
    
    def processItem(self, item:dict) -> str:
        for rule in self.rules:
            res = rule.processItem(item)
            if res is not None:
                return res
        
        return 'R'


def parseRule(sRule : str) -> Rule:
    if ':' in sRule: # there is a condition
        splitted = sRule.split(':')
        return Rule(splitted[1], Condition(splitted[0]))
    else: # only action
        return Rule(sRule)

def parseFlow(sFlow: str) -> Flow:
    # qqz{s>2770:qs,m<1801:hdj,R}

    flowRulesOpening= sFlow.find('{')
    flowRulesEnding = sFlow.find('}')

    name = sFlow[: flowRulesOpening]
    sRules = sFlow[flowRulesOpening+1:flowRulesEnding]
    rules = []

    for sRule in sRules.split(','):
        rule = parseRule(sRule)
        rules.append(rule)
    
    return Flow(name, rules)

def parseItem(sItem: str) -> dict: 
    # {x=787,m=2655,a=1222,s=2876}
    sValues = sItem.strip().removeprefix('{').removesuffix('}').split(',')

    item = {}

    for value in sValues:
        key, val = value.split('=')
        item[key] = int(val)

    return item


