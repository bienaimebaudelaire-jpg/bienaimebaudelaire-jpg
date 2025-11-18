#!/usr/bin/env python3
"""
?? Test du syst?me d'auto-am?lioration HUMEAN
"""

from src.core.humean_auto_improvement import humean_auto_improver

def test_auto_improvement():
    print("?? TEST AUTO-AM?LIORATION HUMEAN")
    print("=" * 50)
    
    # Lancer l'auto-am?lioration
    result = humean_auto_improver.analyze_and_apply(
        "Analyse ton infrastructure et applique les am?liorations critiques"
    )
    
    # Afficher les r?sultats
    print(f"?? Analyse: {len(result['analysis']['identified_issues'])} probl?mes identifi?s")
    print(f"?? Plan: {result['improvement_plan']['total_actions']} actions g?n?r?es")
    print(f"?? Impl?mentation: {result['implementation_results']['completed_actions']} actions compl?t?es")
    
    print("\n?? FICHIERS CR??S:")
    for detail in result['implementation_results']['details']:
        if detail['status'] == 'COMPLETED':
            print(f"   ? {detail['file']} - {detail['impact']}")
    
    print("\n?? HUMEAN s'est auto-am?lior? avec succ?s!")

if __name__ == "__main__":
    test_auto_improvement()

