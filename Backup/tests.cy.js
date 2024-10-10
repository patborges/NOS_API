
// ------------------------ ON STANDBY ------------------------ //
// FOR E2E TESTS BUT NOT APPLIED BC PROGRAM DOESN'T HAVE UI YET //
// ------------------------------------------------------------ //

describe('API Test', () => {
    // ------ API Request
    it('API request Successful', () => {
        cy.request('GET', 'https://www.cttcodigopostal.pt/api/v1/4074c2cf8cc941e9baafa631a4dac171/')
        .then(response => {
            // Assert that the API request was successful
            expect(response.status).to.eq(200);
            expect(response.body).to.have.property('data');
        });
    })

    it('API request error', () => {
        cy.request('GET', 'https://www.cttcodigopostal.pt/api/v1/4074c2cf8cc941e9baafa631a4dac171/', 'false')
        .then(response => {
            // Assert that the API request was successful
            expect(response.status).to.eq(404);
            expect(response.body).to.have.property('error');
        });
    })
})

describe('CSV file tests', () => {

    // ------ CSV File Reading
    it('reads csv file', () => {
        cy.fixture('codigos_postais.csv').then(csv => {
            // Assert that the CSV file was read correctly
            expect(csv).to.be.a('string');
            expect(csv).to.contain('cp7,concelho,distrito');
        });
    })

    it('writes on csv file', () => {
        cy.writeFile('codigos_postais_filled.csv', 'cp7,concelho,distrito\nrow1,row2,row3').then(() => {
            // Assert that the CSV file was written correctly
            cy.readFile('codigos_postais_filled.csv').then(csv => {
                expect(csv).to.contain('cp7,concelho,distrito\nrow1,row2,row3');
            });
        });
    })
})

describe('DB tests', () => {
    // ------ Database Integration
    it('checks database', () => {
        cy.task('db:query', 'SELECT * FROM geoloc.cp_dist_conc').then(result => {
            // Assert that the database query was successful
            expect(result).to.have.property('rows');
            expect(result.rows).to.have.length(1);
        });
    })
})