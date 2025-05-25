import streamlit as st
import random

level_words = {
    "Level 1": [
        "above", "block", "breeze", "brick", "carpet", "cloud", "drink", "field", "groom", "heat", "jumper",
        "oval", "pilot", "plenty", "radio", "silent", "silver", "skill", "stone", "thunder", "verb", "waste",
        "band", "book", "chapter", "drum", "event", "mime", "poem", "scale", "tale", "vote", "beach", "forest",
        "moon", "river", "world", "bark", "nest", "seal", "wombat"
    ],
    "Level 2": [
        "android", "backspin", "billion", "bushfire", "canoe", "cockroach", "cruise", "curtain", "damsel", "edam",
        "fumble", "fountain", "fringe", "gritty", "guest", "pirate", "solar", "stetson", "swagger", "trudge",
        "vanity", "venom", "village", "wharf", "wonderful", "tutu", "police", "weather", "blossom", "python",
        "wolf", "graph", "router", "wireless"
    ],
    "Level 3": [
        "abandon", "accident", "admire", "agenda", "almond", "bargain", "benefit", "brilliant", "coconut", "concede",
        "concoct", "corridor", "crystal", "gorgeous", "hospital", "hypnosis", "inquest", "kitchen", "ledger",
        "malfunction", "marmalade", "minority", "nostalgia", "obsession", "oracle", "original", "pamphlet",
        "paramedic", "pesticide", "prescription", "progression", "surgeon", "quadrangle", "quartet"
    ],
    "Level 4": [
        "adhesive", "aggrieved", "alligator", "anxiety", "bouquet", "burrito", "celebrity", "coerce", "convertible",
        "culminate", "delectable", "effusive", "equivalent", "exhaustive", "gruelling", "humorous", "luxury",
        "miniature", "niche", "opportunity", "paperweight", "participate", "phenomenon", "precursor", "procession",
        "professor", "repetition", "salubrious", "scythe", "secondment", "seniority", "simplicity", "solace",
        "stalwart", "strategist", "transportation", "university", "utopia", "vacancy", "vegetarian", "vicious",
        "volunteer"
    ],
    "Level 5": [
        "aeronautics", "algebra", "augment", "binoculars", "capacious", "chalet", "chiropractor", "colloquial",
        "duplicity", "euphoric", "facade", "hallucinate", "jewellery", "knowledgeable", "monotonous", "pacifist",
        "prosciutto", "psychic", "reminisce", "resuscitate", "succession", "supremacy", "tortellini", "whimsical",
        "wreckage", "elocution", "palindrome", "portraiture", "aristocracy", "coalition", "recession",
        "Afghanistan", "Gallipoli", "Vanuatu", "crustacean", "perennial", "proboscis", "sycamore", "Galileo",
        "percentile", "statistician", "symmetry", "trapezium"
    ]
}

st.set_page_config(page_title="Spelling Bee Generator", layout="centered")
st.title("🐝 Spelling Bee Word Generator")
st.markdown("Pick a level and click to generate a random spelling bee word.")

selected_level = st.selectbox("Choose a spelling level:", list(level_words.keys()))

if st.button("🎲 Generate Word"):
    st.success(f"**{selected_level} Word:** {random.choice(level_words[selected_level])}")
