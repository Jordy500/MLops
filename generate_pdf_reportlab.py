#!/usr/bin/env python3
"""Generate professional PDF report for MLOps project using ReportLab."""

from datetime import datetime
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, Image
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT


def create_report_pdf(output_path: Path) -> None:
    """Create a professional PDF report for the MLOps project."""
    
    # Document setup
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch,
    )
    
    # Story to hold document elements
    story = []
    
    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold',
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
    )
    
    # Title
    story.append(Paragraph("Rapport Mini Projet MLOps", title_style))
    story.append(Paragraph("Wine Quality Prediction", styles['Heading3']))
    story.append(Spacer(1, 0.2*inch))
    
    # Date
    date_text = f"<b>Date:</b> {datetime.now().strftime('%d %B %Y')}"
    story.append(Paragraph(date_text, normal_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Project Information Section
    story.append(Paragraph("📋 Informations du Projet", heading_style))
    
    project_data = [
        ["Champ", "Valeur"],
        ["Nom et Prénom", "Jordan NGUEKO"],
        ["Dataset choisi", "Wine Quality Red (UCI ML Repository)"],
        ["URL du dépôt Git", "https://github.com/Jordy500/MLops"],
        ["Branche par défaut", "main"],
        ["Branche développement", "develop"],
    ]
    
    project_table = Table(project_data, colWidths=[2*inch, 4*inch])
    project_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#ecf0f1')]),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ]))
    
    story.append(project_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Stack Technique
    story.append(Paragraph("🛠️ Stack Technique", heading_style))
    
    stack_data = [
        ["Composant", "Technologie"],
        ["Langage", "Python 3.11"],
        ["ML Framework", "scikit-learn (RandomForest)"],
        ["API", "FastAPI + uvicorn"],
        ["Conteneurisation", "Docker"],
        ["CI/CD", "GitHub Actions"],
        ["Registre Docker", "GitHub Container Registry (GHCR)"],
    ]
    
    stack_table = Table(stack_data, colWidths=[2*inch, 4*inch])
    stack_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#ecf0f1')]),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ]))
    
    story.append(stack_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Livrables
    story.append(Paragraph("✅ Livrables Complétés", heading_style))
    
    story.append(Paragraph("<b>1. Entraînement du modèle</b>", styles['Heading4']))
    story.append(Paragraph(
        "• Fichier: train.py<br/>"
        "• Charge le dataset Wine Quality Red depuis UCI ML Repository<br/>"
        "• Transformation de la variable quality en 3 classes<br/>"
        "• Split train/test (80/20) avec stratification<br/>"
        "• Entraînement d'un RandomForestClassifier<br/>"
        "• <b>Accuracy: 0.7312</b><br/>"
        "• <b>F1-score: 0.7300</b>",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("<b>2. API de Prédiction</b>", styles['Heading4']))
    story.append(Paragraph(
        "• Fichier: main.py<br/>"
        "• Endpoints: GET /health, POST /predict<br/>"
        "• Cohérence des features entre train et predict<br/>"
        "• Utilisation de pandas.DataFrame pour les prédictions",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("<b>3. Dockerisation</b>", styles['Heading4']))
    story.append(Paragraph(
        "• Fichier: Dockerfile<br/>"
        "• Image de base: python:3.11-slim<br/>"
        "• Installation des dépendances<br/>"
        "• Entraînement du modèle lors du build<br/>"
        "• Démarrage de l'API sur le port 8000<br/>"
        "• Image publiée: ghcr.io/jordy500/mlops-wine-quality:latest",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    story.append(Paragraph("<b>4. Pipeline CI/CD</b>", styles['Heading4']))
    story.append(Paragraph(
        "• Feature Training Pipeline (feature/*): Training uniquement - ✅ 30s<br/>"
        "• Develop Release Pipeline (develop): Training + Docker + GHCR - ✅ 1m 23s",
        normal_style
    ))
    story.append(Spacer(1, 0.3*inch))
    
    # Workflow Results
    story.append(Paragraph("🔗 Résultats des Workflows", heading_style))
    
    workflow_data = [
        ["Workflow", "Branch", "Status", "Duration", "URL"],
        [
            "Feature Training",
            "feature/wine-model-upgrade",
            "✅ Success",
            "30s",
            "github.com/.../run/24456896136"
        ],
        [
            "Develop Release",
            "develop",
            "✅ Success",
            "1m 23s",
            "github.com/.../run/24456901847"
        ],
    ]
    
    workflow_table = Table(workflow_data, colWidths=[1.5*inch, 1.5*inch, 0.8*inch, 0.7*inch, 1.3*inch])
    workflow_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#27ae60')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#ecf0f1')]),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
    ]))
    
    story.append(workflow_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Conclusion
    story.append(Paragraph("🎓 Conclusion", heading_style))
    story.append(Paragraph(
        "Ce projet démontre une implémentation complète d'une pipeline MLOps, "
        "du développement local jusqu'à la publication automatisée d'une image Docker via GitHub Actions. "
        "L'architecture est modulaire, testable et prête pour la production.",
        normal_style
    ))
    
    # Footer
    story.append(Spacer(1, 0.5*inch))
    footer_text = f"<font size=8>Rapport généré le {datetime.now().strftime('%d/%m/%Y à %H:%M')}</font>"
    story.append(Paragraph(footer_text, ParagraphStyle('Footer', parent=styles['Normal'], alignment=TA_CENTER)))
    
    # Build PDF
    doc.build(story)
    print(f"✅ PDF report generated: {output_path}")


if __name__ == "__main__":
    repo_path = Path(__file__).parent
    pdf_file = repo_path / "rapport_mlops.pdf"
    
    print(f"Generating PDF report to {pdf_file}...")
    create_report_pdf(pdf_file)
