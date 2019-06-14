def month_to_num(greek):
    if greek == 'ΙΑΝΟΥΑΡΙΟΥ':
        return 1
    if greek == 'ΦΕΒΡΟΥΑΡΙΟΥ':
        return 2
    if greek == 'ΜΑΡΤΙΟΥ':
        return 3
    if greek == 'ΑΠΡΙΛΙΟΥ':
        return 4
    if greek == 'ΜΑΪΟΥ':  # check how meteo type this month
        return 5
    if greek == 'ΙΟΥΝΙΟΥ':
        return 6
    if greek == 'ΙΟΥΛΙΟΥ':
        return 7
    if greek == 'ΑΥΓΟΥΣΤΟΥ':
        return 8
    if greek == 'ΣΕΠΤΕΜΒΡΙΟΥ':
        return 9
    if greek == 'ΟΚΤΩΒΡΙΟΥ':
        return 10
    if greek == 'ΝΟΕΜΒΡΙΟΥ':
        return 11
    if greek == 'ΔΕΚΕΜΒΡΙΟΥ':
        return 12


def day_to_num(day):
    if day == 'Δευτερα':
        return 1
    if day == 'Τριτη':
        return 2
    if day == 'Τεταρτη':
        return 3
    if day == 'Πεμπτη':
        return 4
    if day == 'Παρασκευη':
        return 5
    if day == 'Σαββατο':
        return 6
    if day == 'Κυριακη':
        return 7