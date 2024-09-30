def compare_grades(obj1, obj2):
    # Vérifier si les clés "grades" sont présentes dans les objets
    if "grades" in obj1 and "grades" in obj2:
        grades1 = obj1["grades"]
        grades2 = obj2["grades"]

        # Si les tableaux ont des différences, identifier les nouvelles valeurs
        if grades1 != grades2:
            # Trouver les différences dans grades2 par rapport à grades1
            differences = [grade for grade in grades2 if grade not in grades1]

            # Retourner uniquement les nouvelles valeurs différentes
            if differences:
                return differences
            else:
                return None
        else:
            return None
    else:
        return None
