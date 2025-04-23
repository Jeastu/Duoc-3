from django.db import models

class TipoUsuario(models.Model):
    idTipoUsuario = models.AutoField(primary_key=True, verbose_name="Id del tipo usuario")
    nombreTipo = models.CharField(max_length=30, verbose_name="Nombre del tipo de usuario", null=False, blank=False)

    def __str__(self):
        return self.nombreTipo

    class Meta:
        managed = False
        db_table = 'INICIO_TIPOUSUARIO'


class Usuario(models.Model):
    username = models.CharField(primary_key=True, max_length=15, verbose_name="Username del usuario")
    contrasennia = models.CharField(max_length=30, verbose_name="Contraseña del usuario", null=False, blank=False)
    nombre = models.CharField(max_length=60, verbose_name="Nombre del usuario", null=False, blank=False)
    apellido = models.CharField(max_length=60, verbose_name="Apellido del usuario", null=False, blank=False)
    email = models.CharField(max_length=150, verbose_name="Email del usuario", null=False, blank=False)
    tipousuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'INICIO_USUARIO'


class Comuna(models.Model):
    idComuna = models.AutoField(primary_key=True, verbose_name="Id de comuna", null=False, blank=False)
    nombreCom = models.CharField(max_length=40, verbose_name="Nombre comuna", null=False, blank=False)

    def __str__(self):
        return self.nombreCom

    class Meta:
        managed = False
        db_table = 'INICIO_COMUNA'


class Region(models.Model):
    idRegion = models.AutoField(primary_key=True, verbose_name="Id de region", null=False, blank=False)
    nombreReg = models.CharField(max_length=40, verbose_name="Nombre region", null=False, blank=False)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombreReg

    class Meta:
        managed = False
        db_table = 'INICIO_REGION'


class Direccion(models.Model):
    idDireccion = models.AutoField(primary_key=True, verbose_name="Id de direccion", null=False, blank=False)
    descripcionDir = models.TextField(verbose_name="Descripcion direccion", null=False, blank=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.descripcionDir

    class Meta:
        managed = False
        db_table = 'INICIO_DIRECCION'


class Venta(models.Model):
    idVenta = models.AutoField(primary_key=True, verbose_name="Id de venta", null=False, blank=False)
    fechaVenta = models.DateField(verbose_name="Fecha de venta", null=False, blank=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fechaVenta)

    class Meta:
        managed = False
        db_table = 'INICIO_VENTA'


class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True, verbose_name="ID de la categoria")
    nombreCat = models.CharField(max_length=30, verbose_name="Nombre de la categoria", null=False, blank=False)

    def __str__(self):
        return self.nombreCat

    class Meta:
        managed = False
        db_table = 'INICIO_CATEGORIA'


class TipoProd(models.Model):
    idTiporod = models.AutoField(primary_key=True, verbose_name="ID del tipo producto")
    nombreTipoProd = models.CharField(max_length=60, verbose_name="Nombre del tipo producto", null=False, blank=False)

    def __str__(self):
        return self.nombreTipoProd

    class Meta:
        managed = False
        db_table = 'INICIO_TIPOPROD'


class Marca(models.Model):
    idMarca = models.AutoField(primary_key=True, verbose_name="Id de la marca")
    nombreMarca = models.CharField(max_length=30, verbose_name="Nombre de la marca", null=False, blank=False)

    def __str__(self):
        return self.nombreMarca

    class Meta:
        managed = False
        db_table = 'INICIO_MARCA'


class Modelo(models.Model):
    idModelo = models.AutoField(primary_key=True, verbose_name="Id del modelo")
    nombreModelo = models.CharField(max_length=30, verbose_name="Nombre del modelo", null=False, blank=False)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreModelo

    class Meta:
        managed = False
        db_table = 'INICIO_MODELO'


class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name="Id del Producto")
    nombreProducto = models.CharField(max_length=50, verbose_name="Nombre del Producto", null=False, blank=False)
    precioProducto = models.IntegerField(verbose_name="Precio del Producto", null=False, blank=False)
    especificacionProd = models.CharField(max_length=900, verbose_name="Especificaciones del Producto", null=False, blank=False)
    stockProd = models.IntegerField(verbose_name="Stock del Producto", null=False, blank=False)
    imagenProd = models.ImageField(upload_to="productos", verbose_name="Imagen del Producto", null=True, blank=False)
    tipoprod = models.ForeignKey(TipoProd, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreProducto

    class Meta:
        managed = False
        db_table = 'INICIO_PRODUCTO'


class Detalle(models.Model):
    idDetalle = models.AutoField(primary_key=True, verbose_name="Id del detalle", null=False, blank=False)
    cantidad = models.IntegerField(verbose_name="Cantidad", null=False, blank=False)
    subTotal = models.IntegerField(verbose_name="Subtotal", null=False, blank=False)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.subTotal)

    class Meta:
        managed = False
        db_table = 'INICIO_DETALLE'
