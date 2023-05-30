# Generated by Django 4.1.7 on 2023-05-16 03:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Curso",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=200)),
                ("descricao", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Disciplina",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=200)),
                ("descricao", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Modalidade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Professor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=200)),
                ("matricula", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
            ],
            options={
                "verbose_name": "Professore",
            },
        ),
        migrations.CreateModel(
            name="Turma",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=200)),
                ("descricao", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Reposicao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("conteudo", models.TextField()),
                ("quantidade_aulas", models.CharField(max_length=10)),
                ("data", models.DateField()),
                (
                    "data_hora_inicio",
                    models.TimeField(default=django.utils.timezone.now),
                ),
                ("data_hora_fim", models.TimeField(default=django.utils.timezone.now)),
                (
                    "curso",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="sisar.curso"
                    ),
                ),
                (
                    "disciplina",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="disciplina_reposicao_set",
                        to="sisar.disciplina",
                    ),
                ),
                (
                    "disciplina_substituida",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sisar.disciplina",
                    ),
                ),
                (
                    "modalidade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sisar.modalidade",
                    ),
                ),
                (
                    "professor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="professor_reposicao_set",
                        to="sisar.professor",
                    ),
                ),
                (
                    "professor_substituido",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sisar.professor",
                    ),
                ),
                (
                    "turma",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="sisar.turma"
                    ),
                ),
            ],
            options={
                "verbose_name": "Reposicõe",
            },
        ),
        migrations.CreateModel(
            name="Falta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantidade_aulas", models.CharField(max_length=10)),
                ("data", models.DateField()),
                (
                    "data_hora_inicio",
                    models.TimeField(default=django.utils.timezone.now),
                ),
                ("data_hora_fim", models.TimeField(default=django.utils.timezone.now)),
                ("data_limite_para_reposicao", models.DateField()),
                (
                    "curso",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sisar.curso",
                        verbose_name="Curso",
                    ),
                ),
                (
                    "disciplina",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sisar.disciplina",
                    ),
                ),
                (
                    "modalidade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sisar.modalidade",
                        verbose_name="Modalidade",
                    ),
                ),
                (
                    "professor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sisar.professor",
                    ),
                ),
                (
                    "turma",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sisar.turma",
                        verbose_name="Turma",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Antecipacao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("conteudo", models.TextField()),
                ("quantidade_aulas", models.CharField(max_length=10)),
                ("data", models.DateField()),
                (
                    "data_hora_inicio",
                    models.TimeField(default=django.utils.timezone.now),
                ),
                ("data_hora_fim", models.TimeField(default=django.utils.timezone.now)),
                (
                    "curso",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="sisar.curso"
                    ),
                ),
                (
                    "disciplina",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="disciplina_antecipacao_set",
                        to="sisar.disciplina",
                    ),
                ),
                (
                    "disciplina_substituida",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sisar.disciplina",
                    ),
                ),
                (
                    "modalidade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sisar.modalidade",
                    ),
                ),
                (
                    "professor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="professor_antecipacao_set",
                        to="sisar.professor",
                    ),
                ),
                (
                    "professor_substituido",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sisar.professor",
                    ),
                ),
                (
                    "turma",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="sisar.turma"
                    ),
                ),
            ],
            options={
                "verbose_name": "Antecipaçõe",
            },
        ),
    ]