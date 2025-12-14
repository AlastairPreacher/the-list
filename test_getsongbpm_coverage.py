#!/usr/bin/env python3
"""
Test GetSongBPM API coverage for 'Murder on the Dancefloor' playlist
"""

import requests
import json
import time
from urllib.parse import quote

API_KEY = "f5dfad7e75c4b716e0ce0d62ad05562d"
BASE_URL = "https://api.getsong.co/search/"

# All 100 tracks from playlist (first batch)
tracks = [
    {"name": "Run", "artists": ["MPH", "EV", "Chris Lorenzo"], "id": "16iHE1uKRvAKd1Mt13udlV"},
    {"name": "NOW", "artists": ["Oppidan"], "id": "2957N2fOpFu3HhAAyrzzoz"},
    {"name": "ABC's", "artists": ["MPH", "AntsLive"], "id": "5VEhGGpGA38ZiQRXhWgOTG"},
    {"name": "Just Like", "artists": ["MPH"], "id": "7irbhODkTYtv3aTOze7ts1"},
    {"name": "DARWIN", "artists": ["Oppidan"], "id": "24caY3L0inVduxmvqNfrzj"},
    {"name": "Raw", "artists": ["MPH"], "id": "2U9RtZORzcu54vkWI19PIL"},
    {"name": "one2three (feat. Leven Kali)", "artists": ["Disclosure", "Chris Lake", "Leven Kali"], "id": "6dQxsPVLqXnJgiLLWJRE5x"},
    {"name": "A Place You Wanna Go (Good Life)", "artists": ["bullet tooth"], "id": "0aDKvLIttZfWCA0zFjVn92"},
    {"name": "Bump That", "artists": ["BRUX", "Frazer Ray"], "id": "5yUtKWNHogX0A6LdE7SgU0"},
    {"name": "Dappa Dan", "artists": ["Y U QT", "Diffrent"], "id": "6atT69esWSadQ7Ujx27Z3l"},
    {"name": "IMMACULATE SKANK", "artists": ["bullet tooth"], "id": "678ey4hhnfoCIRYbQ9dTwc"},
    {"name": "Fool Me Twice", "artists": ["BAKEY"], "id": "7JClWYi1C90K4OmS9TyJ6V"},
    {"name": "Until The Morning", "artists": ["MPH"], "id": "2uFTRPIOJCAv3VPDdpQB85"},
    {"name": "Get Dumb", "artists": ["Sammy Virji", "MPH"], "id": "3UZn0r01qyD1UqckgmIsll"},
    {"name": "Clocked It Got Long (Bonus Track)", "artists": ["Bailey Ibbs"], "id": "3myHWah51kXTH8KrDg4eGC"},
    {"name": "I Cannot", "artists": ["Anti Up"], "id": "7rgnKPJ51NBGP5k20yaSHn"},
    {"name": "LOSE YOUR HEAD", "artists": ["Kelly Lee Owens"], "id": "3iWarmifsPD56ys6TBuN9N"},
    {"name": "Fogo", "artists": ["Yo Speed"], "id": "4GVLHnuLDa5VlnFGE8FlDe"},
    {"name": "How You Move - Edit", "artists": ["Charlotte de Witte"], "id": "1biKqdOsiIo2JekJ8UPX1x"},
    {"name": "Blade", "artists": ["D'Angello & Francis"], "id": "1wQwTyocYlAE27QEk8BQXa"},
    {"name": "Aluga", "artists": ["Ma Sha"], "id": "0IKZozc89S4bydkrr66ZCG"},
    {"name": "Try & Escape", "artists": ["Zero"], "id": "0cNDDA6wf2JRpLaKDcPMPl"},
    {"name": "Comin", "artists": ["Kink"], "id": "2NTaAUg7XX76RPBQKyWzM0"},
    {"name": "JOYTOY", "artists": ["Artonal"], "id": "2TZ2uBFfyGaB8a664Nd10V"},
    {"name": "Watch Your Pin", "artists": ["Povoa"], "id": "0RXaZZjZsgdVKJgLWIfQ7Z"},
    {"name": "GET TWISTED", "artists": ["SICARIA", "Lou Nour"], "id": "1FIh7Npu1egJ3cWV6kKUyo"},
    {"name": "Career Advice", "artists": ["HYBRD", "Alan Fitzpatrick"], "id": "400yp7PlC9LLPqX5Gi8M8D"},
    {"name": "Convolve", "artists": ["Bowser"], "id": "2DdNWzLRyxw0aY8XztQ2Qx"},
    {"name": "Flump", "artists": ["Cesco"], "id": "6OSswcrCIZz2D93uC8z9vh"},
    {"name": "Lose My Mind", "artists": ["Champion", "Interplanetary Criminal", "Crookers"], "id": "1LdRvKZka9ZHunz6eoH5B9"},
    {"name": "Dominator", "artists": ["Boys Noize", "Human Resource"], "id": "7oZ8KZELVocU8WY2Ye7b3x"},
    {"name": "Jump Up Quickly - Zero Remix", "artists": ["Mungo's Hi Fi", "Zero", "Soom T"], "id": "50RMgtg1y4rolRtEdinzlO"},
    {"name": "Alarm Bells - Efan Remix", "artists": ["Manga Saint Hilare", "MoreNight", "P Money", "Jme", "efan"], "id": "7pPBJJ2pNJTbJ43ccomWdk"},
    {"name": "IO", "artists": ["Schwefelgelb"], "id": "2WAVAcW9TlnkChZrXj5W4K"},
    {"name": "Afterparty", "artists": ["CLIFFORD"], "id": "2ozUtemjsy7OuFo5BHoVn8"},
    {"name": "I'm Really Hot (For Myself)", "artists": ["Mura Masa"], "id": "0Ot136xJA9ghl1JR5eaaVS"},
    {"name": "Party Rock", "artists": ["DJ Fuckoff"], "id": "2OwVcCUZa2C08NVIPyZM6j"},
    {"name": "Moaner", "artists": ["Underworld"], "id": "42MDEG1z2DNSAtx8y0jZ6u"},
    {"name": "E After Next", "artists": ["Avalon Emerson", "Moby"], "id": "1yb4K5pUkIfRZIw32ZaTvx"},
    {"name": "Tambourine", "artists": ["The Dare"], "id": "3eIhHWOMaTAPvJ6azg0b2L"},
    {"name": "Beat Bunny", "artists": ["Povoa", "Madge"], "id": "03aGl91oeW7EZolJTFFNlM"},
    {"name": "Block Rockin' Beats - Don Diablo Remix", "artists": ["The Chemical Brothers", "Don Diablo"], "id": "4mIQn3WT3fW0XqaMVRvMl0"},
    {"name": "Onda", "artists": ["Piezo", "Priori"], "id": "4tHMwlnLreWjSR3rPQ2Vsr"},
    {"name": "SPEAKERS - VIP MIX", "artists": ["Hyas", "Pura Pura"], "id": "33I46YeNNJZRNPACu26swQ"},
    {"name": "Too Slow (All Night)", "artists": ["Eliza Rose", "Oppidan"], "id": "4ywDQlrX9XdJB19bvl3cvU"},
    {"name": "Come With It - Bumpty Mix", "artists": ["Sam Binga"], "id": "6lMhz0W9cF8vjSVzA0KZBP"},
    {"name": "Expand", "artists": ["Nitepunk", "Harrison Clayton"], "id": "7c5FCKhwGFvHiqQfUwrdPd"},
    {"name": "Bend Ya Back", "artists": ["Prozak"], "id": "6GYlRam9f1LNxZbR7gYqi9"},
    {"name": "Metronome - Mixed", "artists": ["Yo Speed"], "id": "6NUGmgqaG8Sj1N0LtOFScU"},
    {"name": "Say Less", "artists": ["Bailey Ibbs"], "id": "5dItRJ9nTweovbE8YPeQwu"},
    {"name": "whats bitting you?", "artists": ["Vladimir Dubyshkin"], "id": "2FcehqMAl5ANMenA1TlCA6"},
    {"name": "Navalha", "artists": ["Nørbak"], "id": "5eC8qs7v1Rw6U0T7mTNVA8"},
    {"name": "Get Ur Freak On", "artists": ["BEAUZ", "JKRS", "NIVEK"], "id": "3ehFMmXnxE1O5Gxi3yycAw"},
    {"name": "We'll Be Back", "artists": ["Charlie Boon"], "id": "64ZSbsECsGeoZq8dhYkUiM"},
    {"name": "Rocinha", "artists": ["Bombo Rosa"], "id": "29Mw1mBFrgS7wKDnjdDO0F"},
    {"name": "Joss Bay - Club Mix", "artists": ["Kassian"], "id": "6mQ9x7RD4raegntPkJOL6M"},
    {"name": "Something In Me", "artists": ["DJ Hybrid"], "id": "0Ck9XZ0Wia2hjwDY1Oh6A1"},
    {"name": "sealight", "artists": ["fia"], "id": "0RBuMInsBUvxIirprg2U7Q"},
    {"name": "Like It - Randomer Remix", "artists": ["Purient", "Randomer"], "id": "18JusSAKIhWOuUiJNRxmqg"},
    {"name": "The Realm", "artists": ["Charlotte de Witte"], "id": "5oUM6niJ1fzxxSTah13Osf"},
    {"name": "CHROMA 011 A.L.O.E II", "artists": ["BICEP", "B.D.B", "Benjamin Damage"], "id": "61gCDJBdaNXE4sy9Xl2lvl"},
    {"name": "Native Wit", "artists": ["X CLUB."], "id": "6G2VuvrfFsLddKNhxHdzfy"},
    {"name": "All The DJs", "artists": ["Patrick Topping"], "id": "12iWPV4rYVfR8RftPMZd4W"},
    {"name": "Different", "artists": ["Barry Can't Swim"], "id": "0FPxUQoBxCSY8Cze1BW0vs"},
    {"name": "Something French", "artists": ["Getdown Services"], "id": "3s9kEtw8SwAg4GTKlTcMcq"},
    {"name": "Keepmastik - Taiki Nulight Remix", "artists": ["Phlegmatic Dogs", "Taiki Nulight"], "id": "4egiouZis0RPnfHYOV5dAs"},
    {"name": "Faux - KiNK Remix", "artists": ["Blakkat", "Kink"], "id": "6gxgweAnEAsI3fMWjnEjTJ"},
    {"name": "Love Up High", "artists": ["Pricila Diaz", "Linkage"], "id": "4pkQ33FKph0gIczq2cf3CC"},
    {"name": "ASCEND", "artists": ["Kelly Lee Owens"], "id": "20cOEyAbHE1aq1FUaPCs1N"},
    {"name": "Cabin Dance", "artists": ["Octo Octa"], "id": "1T4bQrsOpmeNuOnvVFpAGo"},
    {"name": "Let Me Clear My Throat", "artists": ["Devault"], "id": "7dP5EtY64b0dWwcWXb8Xlq"},
    {"name": "Lose Control", "artists": ["Crusy", "David LeSal"], "id": "29ckDhEsLydghxneMmTBLa"},
    {"name": "After Time - Adana Twins Remix", "artists": ["Nic Fanciulli", "Adana Twins"], "id": "7a8nnQeoQ7URKBellEdI1j"},
    {"name": "Deadlock", "artists": ["MPH"], "id": "6QxthyU2TkJvKQ93bualUb"},
    {"name": "Allbarone", "artists": ["Baxter Dury", "JGrrey"], "id": "041DJ4hUI6drOqYgLf3QQG"},
    {"name": "Josephine", "artists": ["Daphni"], "id": "0l7JCXzezE7Gm7muaklAaK"},
    {"name": "One Chance", "artists": ["Cameo Blush"], "id": "0XnH6eXRTsSJoFQGUh0I6z"},
    {"name": "Paradise Runner", "artists": ["Overmono"], "id": "3L7TOZvbuTsxH5EM8LVHUZ"},
    {"name": "Insomnia - Disclosure's 2025 Edit", "artists": ["Faithless", "Disclosure"], "id": "4cgoqLcfYRBesDEmSVR1Ek"},
    {"name": "Let Me Tell U SMTH", "artists": ["A.M.C"], "id": "35il5XJ3JrbzNRpSVIfBDa"},
    {"name": "Ouais Ouais Ouais", "artists": ["Bok Bok"], "id": "1YAAcPkIJtn6N3PWBNvC33"},
    {"name": "Ear Pressure", "artists": ["Ma Sha"], "id": "0C8cFdVVVhAhsOomoNy3r5"},
    {"name": "Sinsahoi", "artists": ["Dario Nunez", "Javi Colina"], "id": "7yWsj3ZEgGVnAOk8ZNKmuQ"},
    {"name": "Surrender", "artists": ["RUZE", "Josh Butler"], "id": "0YBy9MSILEYi7XkaFFvUSi"},
    {"name": "Slinky - Bakery Edit", "artists": ["Dj Streaks"], "id": "7fFZLw5Oz27ul6vyh6KPWf"},
    {"name": "Business", "artists": ["Fold", "cu.rve"], "id": "3B7DEjXs1lyFLHGqtxjSbq"},
    {"name": "Girls", "artists": ["The Dare"], "id": "7m8wiHGjtlJ5UQvqiCjhV5"},
    {"name": "NO CAP", "artists": ["Disclosure", "Anderson .Paak"], "id": "6zaeVCwnf3A9S8R7QfDHQW"},
    {"name": "Cvlt", "artists": ["Yo Speed"], "id": "4pd7zQ0NowYvgd1yiOjrGu"},
    {"name": "Lick & Pop It", "artists": ["p-rallel"], "id": "46g7bpCuXApVHkB5VkuMWK"},
    {"name": "BEN", "artists": ["Fakear", "oOgo", "Laaanky", "Aksel Aksel", "Club Nowadays"], "id": "4vpt0wptg6Od7vt4vyIx8h"},
    {"name": "Sweatbox", "artists": ["Harry Wills", "Mikey Sebastian"], "id": "7rrE7xPl4rE26gvcXagLf3"},
    {"name": "Dumb Dumb", "artists": ["Decius"], "id": "5xQyNHNEDGqcYeWzIRDV0P"},
    {"name": "Revolution", "artists": ["Paranoid London"], "id": "5DoVmmEKkp3UFY3VuFHZi4"},
    {"name": "Decimated Driver - Dub", "artists": ["Paranoid London", "Water Machine"], "id": "1lGvMBVOrxSC5ipSz7XmBU"},
    {"name": "Trent - Knee Jerk Mix", "artists": ["Hodge"], "id": "0g0SocdFIml7gacZB4X0DY"},
    {"name": "Limoncello - Club Mix", "artists": ["Kassian"], "id": "3EiwiBeCuCbx2U36fmqPs8"},
    {"name": "Push", "artists": ["Tony Dark Eyes"], "id": "2lbXd90vTTuCUCZ6tKaxPl"},
    {"name": "Push Up", "artists": ["Wax Motif", "Kyle Watson", "Scrufizzer"], "id": "6CqfT2mBl9VLQhtqoyhOOh"},
    {"name": "NONSTOP", "artists": ["Darby"], "id": "585I7WDRPBBNo1aLv9lOyH"}
]

def test_track(track):
    """Test a single track against GetSongBPM API"""
    # Build search query: track name + first artist
    artist = track['artists'][0] if track['artists'] else ""
    query = f"{track['name']} {artist}"

    url = f"{BASE_URL}?api_key={API_KEY}&type=song&lookup={quote(query)}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            # Check if we got results
            if 'search' in data and len(data['search']) > 0:
                # Found the track
                song = data['search'][0]  # Take first result
                return {
                    'found': True,
                    'track': track['name'],
                    'artist': artist,
                    'bpm': song.get('tempo'),
                    'key': song.get('key_of'),
                    'danceability': song.get('danceability'),
                    'acousticness': song.get('acousticness')
                }
            else:
                # No results
                return {
                    'found': False,
                    'track': track['name'],
                    'artist': artist,
                    'reason': 'No results in database'
                }
        else:
            # API error
            return {
                'found': False,
                'track': track['name'],
                'artist': artist,
                'reason': f'API error: {response.status_code}'
            }
    except Exception as e:
        return {
            'found': False,
            'track': track['name'],
            'artist': artist,
            'reason': f'Exception: {str(e)}'
        }

def main():
    print(f"Testing {len(tracks)} tracks against GetSongBPM API...")
    print(f"API Key: {API_KEY[:8]}...")
    print("-" * 80)

    found_tracks = []
    missing_tracks = []

    for i, track in enumerate(tracks, 1):
        print(f"[{i}/{len(tracks)}] Testing: {track['name']} - {track['artists'][0]}")

        result = test_track(track)

        if result['found']:
            found_tracks.append(result)
            print(f"  ✓ FOUND - BPM: {result.get('bpm')}, Key: {result.get('key')}, Dance: {result.get('danceability')}")
        else:
            missing_tracks.append(result)
            print(f"  ✗ MISSING - {result.get('reason')}")

        # Rate limiting: wait 0.5s between requests to avoid hitting limits
        if i < len(tracks):
            time.sleep(0.5)

    print("\n" + "=" * 80)
    print("FINAL RESULTS")
    print("=" * 80)
    print(f"Total tracks tested: {len(tracks)}")
    print(f"Found in GetSongBPM: {len(found_tracks)}")
    print(f"Missing from GetSongBPM: {len(missing_tracks)}")
    print(f"Coverage: {(len(found_tracks) / len(tracks)) * 100:.2f}%")
    print("=" * 80)

    # Save detailed results
    results = {
        'total': len(tracks),
        'found': len(found_tracks),
        'missing': len(missing_tracks),
        'coverage_percent': (len(found_tracks) / len(tracks)) * 100,
        'found_tracks': found_tracks,
        'missing_tracks': missing_tracks
    }

    with open('getsongbpm_results.json', 'w') as f:
        json.dump(results, f, indent=2)

    print("\nDetailed results saved to: getsongbpm_results.json")

    # Print missing tracks summary
    print("\nMISSING TRACKS:")
    print("-" * 80)
    for track in missing_tracks[:20]:  # Show first 20
        print(f"  • {track['track']} - {track['artist']}")
    if len(missing_tracks) > 20:
        print(f"  ... and {len(missing_tracks) - 20} more")

if __name__ == "__main__":
    main()
