"""Premium prompts for the 4 transcendent skills: 5 distinct concepts each."""
STYLE = ("legendary transcendent ultimate skill icon, {subject}, iridescent violet and cyan arcane light "
         "with radiant celestial gold accents, ornate sacred geometry, cinematic volumetric god rays, "
         "luxurious and divine, ultra detailed masterpiece, epic scale, painterly digital fantasy art, "
         "deep midnight navy cosmos background, centered symmetrical composition, breathtaking, no text, no letters")
C = {
 "sk-14": [  # Sovereign's Hijack
  "a colossal enemy archmage's world-ending spell circle frozen mid-cast in the sky, thousands of its glowing threads being pulled away by one small calm hand below, the spell turning around to face its caster",
  "a crowned silhouette standing on a battlefield, every enemy's mana rising as ribbons of light and converging into a radiant floating crown above his head, enemies kneeling",
  "a giant celestial chessboard where the enemy king's glowing spell pieces are being moved by a single elegant hand from above, pieces turning to his color",
  "an enormous divine hand of light reaching down from cracked heavens and plucking a blazing ultimate spell out of an enemy's grasp like stealing a star",
  "a throne made of captured enemy spells and magic circles, a hooded young mage lounging on it casually with one leg crossed, rivers of stolen mana flowing to him",
 ],
 "sk-15": [  # Abyssal Singularity
  "a perfect black singularity sphere with a blazing violet and gold accretion halo, an entire battlefield of mana spiraling into it like a galaxy, space itself bending",
  "a lone mage holding a tiny black star in his palm while a whole sky of light, rivers and auroras are sucked into it, cosmic scale",
  "the moment of collapse, a black hole eye opening in the sky with a golden iris ring, ruins and stars spiraling into the pupil",
  "a cathedral of light imploding toward one black point, stained glass shards and mana streams falling inward, absolute silence",
  "a cosmic flower blooming from a central black void, petals made of compressed mana and starlight swirling inward, divine and terrifying",
 ],
 "sk-a06": [  # Unmeasurable
  "a mage walking forward through a towering wall of nine glowing ranking stars that shatter into golden dust as he passes, stepping out of the frame of the world",
  "an infinite cosmic measuring scale and ruler breaking apart into light, numbers dissolving, a silhouette standing beyond the edge of the measurement",
  "a figure stepping out of a golden picture frame into an endless starry void, the frame labeled by nine stars cracking, everything behind him small",
  "all the mana of a battlefield rising as identical glowing motes, stripped of rank and color, orbiting obediently around a single raised fingertip like a conductor of the cosmos",
  "nine celestial crowns of rank falling and dissolving around a calm hooded mage who stands in the center of a perfect golden circle, untouched by any of them",
 ],
 "sk-p05": [  # Life Resonance
  "an armored warrior with no magic, his heartbeat, blood and breath visible as luminous golden rivers inside his body, being gently bent like harp strings by a mage's fingers",
  "a giant glowing tree of life made of veins and breath, its golden sap flowing through a battlefield of warriors, a mage conducting the flow with one hand",
  "a single glowing heart floating at the center, its pulse sending rings of golden life energy outward, woven with violet mana threads into one harmony",
  "two hands cradling a sphere containing a living heartbeat, golden blood rivers and violet mana intertwining like a double helix around it",
  "a charging barbarian frozen mid-swing as his own life current, shining gold through his muscles and veins, is turned aside by a serene mage touching the air",
 ],
}
def prompt(sid, i): return STYLE.format(subject=C[sid][i])
