#!/usr/bin/env python3
import csv
import re

def clean_csv():
    # Read the original file
    with open('your_first_verbs_backup.csv', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split into lines
    lines = content.split('\n')
    
    # Write clean CSV
    with open('your_first_verbs_clean.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        
        # Write header
        writer.writerow(['Emoji', 'infinitive_verb', 'infinitive_phonetic_us', 'literal_translation', 'contextual_translation', 'infinitive_phonetic_uk'])
        
        # Process each line manually
        for i, line in enumerate(lines[1:], 1):
            if not line.strip():
                continue
                
            # Find the positions of commas that are not inside quotes
            parts = []
            current_part = ""
            in_quotes = False
            
            for char in line:
                if char == '"':
                    in_quotes = not in_quotes
                elif char == ',' and not in_quotes:
                    parts.append(current_part.strip())
                    current_part = ""
                    continue
                current_part += char
            
            # Add the last part
            if current_part.strip():
                parts.append(current_part.strip())
            
            if len(parts) >= 6:
                emoji = parts[0]
                verb = parts[1]
                phonetic_us = parts[2]
                literal = parts[3].strip('"')
                contextual = parts[4].strip('"')
                phonetic_uk = parts[5]
                
                writer.writerow([emoji, verb, phonetic_us, literal, contextual, phonetic_uk])
                print(f'Line {i}: {verb} - US: {phonetic_us}, UK: {phonetic_uk}')

if __name__ == "__main__":
    clean_csv()
