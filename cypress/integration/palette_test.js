describe('Prueba  app VRT_colorPallete', function() {
	
	it('Va a VRT_colorPallete y genera dos paletas de colores', function() {
        cy.visit('https://alfyes.github.io/VRT_colorPallete/')
		
		cy.contains('Generar nueva paleta').click()

		cy.screenshot('primerpantallazo')

		cy.contains('Generar nueva paleta').click()

		cy.screenshot('segundopantallazo')
	})
})
