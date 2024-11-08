# Generated by Django 5.1.3 on 2024-11-07 19:33

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductoFinanciero",
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
                ("nombre", models.CharField(max_length=100)),
                ("descripcion", models.TextField()),
                (
                    "tasa_retorno",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Tasa de retorno anual en porcentaje",
                        max_digits=5,
                    ),
                ),
                ("plazo", models.IntegerField(help_text="Plazo de inversión en meses")),
                (
                    "riesgo",
                    models.CharField(
                        choices=[
                            ("bajo", "Bajo"),
                            ("medio", "Medio"),
                            ("alto", "Alto"),
                        ],
                        default="medio",
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("direccion", models.CharField(blank=True, max_length=255, null=True)),
                ("telefono", models.CharField(blank=True, max_length=15, null=True)),
                ("fecha_nacimiento", models.DateField(blank=True, null=True)),
                (
                    "perfil_riesgo",
                    models.CharField(
                        choices=[
                            ("bajo", "Bajo"),
                            ("medio", "Medio"),
                            ("alto", "Alto"),
                        ],
                        default="medio",
                        max_length=50,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Los grupos a los que pertenece el usuario.",
                        related_name="usuario_groups",
                        to="auth.group",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Permisos específicos de usuario.",
                        related_name="usuario_user_permissions",
                        to="auth.permission",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Inversion",
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
                (
                    "monto",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Monto invertido en moneda local",
                        max_digits=10,
                    ),
                ),
                ("fecha_inversion", models.DateField(auto_now_add=True)),
                (
                    "producto_financiero",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.productofinanciero",
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.usuario"
                    ),
                ),
            ],
        ),
    ]