from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
#from django.utils.translation import ugettext_lazy as _

from .models import User,Address,Bill


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)



@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    #add address
    fields= ['lot', 'street_num', 'street'  ]
    #
    list_display = ('lot', 'street_num', 'street')

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    #add Bill
    fields=['dscpt_text', 'amt', 'due_date' ,  'paid' , 'address' , 'owner']
    #list/view Bills
    list_display = ( 'dscpt_text' , 'amt', 'due_date' , 'paid' , 'address' , 'owner')
