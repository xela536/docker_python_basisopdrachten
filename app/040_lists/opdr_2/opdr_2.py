# Opdracht 2 lists
# Naam student:
# Groep:

rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

print (rivieren[0].capitalize(), "stroomt onder andere door", rivier_info["rijn"][1].capitalize())
print (rivieren[1].capitalize(), "stroomt onder andere door", rivier_info["maas"][0].capitalize())
print (rivieren[2].capitalize(), "stroomt onder andere door", rivier_info["nijl"][2].capitalize())





