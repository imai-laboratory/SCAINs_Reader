def summary_chat_ja(dialogue, sentence):
    joined_dialogue = "\n".join(dialogue)
    prompt = f"以下はAとBの2人の会話です．この会話を「{sentence}」の観点から2文程度で説明してください．\n\n{joined_dialogue}"
    return prompt

def summary_comp_ja(dialogue, sentence):
    joined_dialogue = "\n".join(dialogue)
    prompt = f"会話文をある文の観点から説明します．AとBの2人の会話文が入力され，観点となる文が指定されます．指定された文がどういうことを言っているか，会話文全体を踏まえて2文程度で説明します．\n\n# 会話文\n{joined_dialogue}\n\n# 観点\n{sentence}\n\n# 説明\n"
    return prompt

def rephrase_chat_ja(dialogue, sentence):
    joined_dialogue = "\n".join(dialogue)
    prompt = f"会話文中のある発言を具体的に言い換えます．\nAとBの2人の会話文が入力され，言い換えの対象となる発言が指定されます．\n指定された発言を，会話文中の言葉を使ってより具体的に言い換えます．\n\n# 会話文\n{joined_dialogue}\n\n# 言い換える発言\n{sentence}\n\n# 具体的な発言\n"
    return prompt

def important_chat_ja(dialogue):
    numbered_dialogue = []
    for idx, utterance in enumerate(dialogue):
        numbered_dialogue.append(str(idx + 1) + ". " + utterance)
    joined_dialogue = "\n".join(numbered_dialogue)
    prompt = f"会話文から最も重要な発言を選びます．発言に番号をつけた一連の会話文が入力されます．会話文から最も重要な発言を2つ選び，その番号を書きます．\n\n# 出力の形式\n[発言の番号1, 発言の番号2]\n\n# 会話文\n{joined_dialogue}\n\n# 重要な発言\n"
    return prompt