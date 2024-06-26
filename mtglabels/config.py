API_ENDPOINT = "https://api.scryfall.com/sets"

# Set types we are interested in
SET_TYPES = (
    "core",
    "expansion",
    "starter",  # Portal, P3k, welcome decks
    "masters",
    "commander",
    "planechase",
    "draft_innovation",  # Battlebond, Conspiracy
    "duel_deck",  # Duel Deck Elves,
    "premium_deck",  # Premium Deck Series: Slivers, Premium Deck Series: Graveborn
    "from_the_vault",  # Make sure to adjust the MINIMUM_SET_SIZE if you want these
    "archenemy",
    "box",
    "funny",  # Unglued, Unhinged, Ponies: TG, etc.
    # "memorabilia",  # Commander's Arsenal, Celebration Cards, World Champ Decks
    # "spellbook",
    # These are relatively large groups of sets
    # You almost certainly don't want these
    # "token",
    # "promo",
)

# Only include sets at least this size
# For reference, the smallest proper expansion is Arabian Nights with 78 cards
MINIMUM_SET_SIZE = 50

# Set codes you might want to ignore
IGNORED_SETS = (
    "cmb1",  # Mystery Booster Playtest Cards
    "amh1",  # Modern Horizon Art Series
    "cmb2",  # Mystery Booster Playtest Cards Part Deux
    "fbb",  # Foreign Black Border
    "sum",  # Summer Magic / Edgar
    "4bb",  # Fourth Edition Foreign Black Border
    "bchr",  # Chronicles Foreign Black Border
    "rin",  # Rinascimento
    "ren",  # Renaissance
    "rqs",  # Rivals Quick Start Set
    "itp",  # Introductory Two-Player Set
    "sir",  # Shadows over Innistrad Remastered
    "sis",  # Shadows of the Past
    "cst",  # Coldsnap Theme Decks
)

# Used to rename very long set names
RENAME_SETS = {
    "Adventures in the Forgotten Realms Minigames": "Forgotten Realms Minigames",
    "Adventures in the Forgotten Realms": "Forgotten Realms",
    "Angels: They're Just Like Us but Cooler and with Wings": "Angels: They're Just Like Us",
    "Archenemy: Nicol Bolas Schemes": "Archenemy: Bolas Schemes",
    "Commander Anthology Volume II": "Commander Anthology II",
    "Commander Legends: Battle for Baldur's Gate": "CMDR Legends: Baldur's Gate",
    "Crimson Vow Commander": "CMDR Crimson Vow",
    "Dominaria United Commander": "CMDR Dominaria United",
    "Duel Decks Anthology: Divine vs. Demonic": "DDA: Divine vs. Demonic",
    "Duel Decks Anthology: Elves vs. Goblins": "DDA: Elves vs. Goblins",
    "Duel Decks Anthology: Garruk vs. Liliana": "DDA: Garruk vs. Liliana",
    "Duel Decks Anthology: Jace vs. Chandra": "DDA: Jace vs. Chandra",
    "Duel Decks: Ajani vs. Nicol Bolas": "DD: Ajani vs. Nicol Bolas",
    "Duel Decks: Blessed vs. Cursed": "DD: Blessed vs. Cursed",
    "Duel Decks: Divine vs. Demonic": "DD: Divine vs. Demonic",
    "Duel Decks: Elspeth vs. Kiora": "DD: Elspeth vs. Kiora",
    "Duel Decks: Elspeth vs. Tezzeret": "DD: Elspeth vs. Tezzeret",
    "Duel Decks: Elves vs. Goblins": "DD: Elves vs. Goblins",
    "Duel Decks: Elves vs. Inventors": "DD: Elves vs. Inventors",
    "Duel Decks: Garruk vs. Liliana": "DD: Garruk vs. Liliana",
    "Duel Decks: Heroes vs. Monsters": "DD: Heroes vs. Monsters",
    "Duel Decks: Jace vs. Chandra": "DD: Jace vs. Chandra",
    "Duel Decks: Knights vs. Dragons": "DD: Knights vs. Dragons",
    "Duel Decks: Merfolk vs. Goblins": "DD: Merfolk vs. Goblins",
    "Duel Decks: Nissa vs. Ob Nixilis": "DD: Nissa vs. Ob Nixilis",
    "Duel Decks: Phyrexia vs. the Coalition": "DD: Phyrexia vs. Coalition",
    "Duel Decks: Speed vs. Cunning": "DD: Speed vs. Cunning",
    "Duel Decks: Zendikar vs. Eldrazi": "DD: Zendikar vs. Eldrazi",
    "Forgotten Realms Commander": "CMDR Forgotten Realms",
    "Fourth Edition Foreign Black Border": "Fourth Edition FBB",
    "Global Series Jiang Yanggu & Mu Yanling": "Jiang Yanggu & Mu Yanling",
    "Innistrad: Crimson Vow Minigames": "Crimson Vow Minigames",
    "Introductory Two-Player Set": "Intro Two-Player Set",
    "Kaldheim Commander": "CMDR Kaldheim",
    "March of the Machine Commander": "CMDR March of the Machine",
    "March of the Machine: The Aftermath": "March of the Machine: Aftermath",
    "Midnight Hunt Commander": "CMDR Midnight Hunt",
    "Mystery Booster Playtest Cards 2019": "MB Playtest Cards 2019",
    "Mystery Booster Playtest Cards 2021": "MB Playtest Cards 2021",
    "Mystery Booster Playtest Cards": "Mystery Booster Playtest",
    "Mystery Booster Retail Edition Foils": "Mystery Booster Retail Foils",
    "Neon Dynasty Commander": "CMDR Neon Dynasty",
    "New Capenna Commander": "CMDR New Capenna",
    "Phyrexia: All Will Be One Commander": "CMDR Phyrexia: One",
    "Planechase Anthology Planes": "Planechase Anth. Planes",
    "Premium Deck Series: Fire and Lightning": "PD: Fire & Lightning",
    "Premium Deck Series: Graveborn": "Premium Deck Graveborn",
    "Premium Deck Series: Slivers": "Premium Deck Slivers",
    "Starter Commander Decks": "CMDR Starter Decks",
    "Strixhaven: School of Mages Minigames": "Strixhaven Minigames",
    "Tales of Middle-earth Commander": "CMDR The Lord of the Rings",
    "The Brothers' War Commander": "CMDR The Brothers' War",
    "The Brothers' War Retro Artifacts": "The Brothers' War Retro",
    "The Lord of the Rings: Tales of Middle-earth": "The Lord of the Rings",
    "The Lost Caverns of Ixalan Commander": "CMDR Lost Caverns of Ixalan",
    "Warhammer 40,000 Commander": "CMDR Warhammer 40K",
    "Wilds of Eldraine Commander": "CMDR Wilds of Eldraine",
    "World Championship Decks 1997": "World Championship 1997",
    "World Championship Decks 1998": "World Championship 1998",
    "World Championship Decks 1999": "World Championship 1999",
    "World Championship Decks 2000": "World Championship 2000",
    "World Championship Decks 2001": "World Championship 2001",
    "World Championship Decks 2002": "World Championship 2002",
    "World Championship Decks 2003": "World Championship 2003",
    "World Championship Decks 2004": "World Championship 2004",
    "Zendikar Rising Commander": "CMDR Zendikar Rising",
}


LETTER_WIDTH = 2160  # Letter paper width in mm
LETTER_HEIGHT = 2790  # Letter paper height in mm
