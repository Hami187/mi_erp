from django.db import models


class Departamento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['nombre']


class Empleado(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]

    cedula = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)
    cargo = models.CharField(max_length=200)
    salario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['apellido', 'nombre']


class Nomina(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('pagada', 'Pagada'),
        ('anulada', 'Anulada'),
    ]

    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    mes = models.IntegerField()
    anio = models.IntegerField()
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    bonificaciones = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    descuentos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_pago = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total = self.salario_base + self.bonificaciones - self.descuentos
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Nómina {self.empleado} - {self.mes}/{self.anio}'

    class Meta:
        verbose_name = 'Nómina'
        verbose_name_plural = 'Nóminas'
        ordering = ['-anio', '-mes']